"""一键录入公开语料到 data/raw（按业务域分子目录），并自动登记 data/source_manifest.md。

用法（项目根目录）：
  python scripts\ingest_sources.py --cmrc 100 --drcd 80
  python scripts\ingest_sources.py --langchain-dir <已解压的仓库目录>
  python scripts\ingest_sources.py --wiki 120
  python scripts\ingest_sources.py --thucnews 150

来源（已与用户确认，全部为真实公开来源）：
  cmrc     CMRC2018 中文机器阅读理解（学术用途） https://github.com/ymcui/CMRC2018
  drcd     DRCD 台达阅读理解（CC BY-SA 3.0，繁体） https://github.com/DRCKnowledgeTeam/DRCD
  langchain Langchain-Chatchat 中文文档（开源）  https://github.com/chatchat-space/Langchain-Chatchat
  wiki     中文维基百科（CC BY-SA 4.0）        https://dumps.wikimedia.org/zhwiki/latest/（经 HF 清洗数据集加载）
  thucnews THUCNews 清华新闻（学术用途）        http://thuctc.thunlp.org/
"""

import argparse
import base64
import json
import subprocess
import sys
import urllib.parse
import zipfile
from datetime import date
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
MANIFEST = Path(__file__).parent.parent / "data" / "source_manifest.md"
TODAY = date.today().isoformat()

GH = {
    "cmrc": ("ymcui", "CMRC2018", "master", "data/cmrc2018_train.json"),
    "drcd": ("DRCKnowledgeTeam", "DRCD", "master", "DRCD_training.json"),
}
LICENSE = {
    "cmrc": "学术用途（非商业）", "drcd": "CC BY-SA 3.0",
    "langchain": "开源（GitHub 公开仓库）", "wiki": "CC BY-SA 4.0",
    "thucnews": "Apache-2.0（THUCNews 镜像）",
}
SRC_URL = {
    "cmrc": "https://github.com/ymcui/CMRC2018",
    "drcd": "https://github.com/DRCKnowledgeTeam/DRCD",
    "langchain": "https://github.com/chatchat-space/Langchain-Chatchat",
    "wiki": "https://dumps.wikimedia.org/zhwiki/latest/",
    "thucnews": "https://huggingface.co/datasets/Tongjilibo/THUCNews",
}


def _curl(url: str, dest: Path, timeout: int = 300):
    r = subprocess.run(["curl.exe", "-sS", "--ssl-no-revoke", "--max-time", str(timeout),
                        "-H", "User-Agent: codex", "-o", str(dest), url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not dest.exists() or dest.stat().st_size == 0:
        raise RuntimeError(f"下载失败: {url} {r.stderr[:200]}")


def _gh_fetch(owner: str, repo: str, branch: str, path: str, timeout: int = 300) -> bytes:
    tree = json.loads(_curl_text(
        f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1", timeout))
    sha = next(t["sha"] for t in tree["tree"] if t["type"] == "blob" and t["path"] == path)
    blob = json.loads(_curl_text(
        f"https://api.github.com/repos/{owner}/{repo}/git/blobs/{sha}", timeout))
    return base64.b64decode(blob["content"])


def _curl_text(url: str, timeout: int = 300) -> str:
    tmp = Path(sys.path[0]).parent / "data" / "_gh_tmp.json"
    _curl(url, tmp, timeout)
    text = tmp.read_text(encoding="utf-8")
    tmp.unlink(missing_ok=True)
    return text


def write_doc(domain: str, filename: str, title: str, text: str, source_key: str):
    d = RAW_DIR / domain
    d.mkdir(parents=True, exist_ok=True)
    body = text.strip()
    if not body:
        return False
    (d / filename).write_text(f"# {title}\n\n{body}", encoding="utf-8")
    n = _next_manifest_no()
    with open(MANIFEST, "a", encoding="utf-8") as f:
        f.write(f"| {n} | data/raw/{domain}/{filename} | {title} | {SRC_URL[source_key]} | {TODAY} | {LICENSE[source_key]} |\n")
    return True


def _next_manifest_no() -> int:
    if not MANIFEST.exists():
        return 1
    n = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            parts = line.split("|")
            if len(parts) > 1 and parts[1].strip().isdigit():
                n = max(n, int(parts[1].strip()))
    return n + 1


def ingest_cmrc(count: int):
    data = json.loads(_gh_fetch(*GH["cmrc"]).decode("utf-8"))
    articles = data if isinstance(data, list) else data.get("data", [])
    ok = 0
    for article in articles:
        if ok >= count:
            break
        title = article.get("title", "CMRC2018")
        text = article.get("context_text", "")
        if write_doc("百科问答", f"cmrc_{ok + 1:03d}.md", title, text, "cmrc"):
            ok += 1
    print(f"[cmrc] 录入 {ok} 篇")
    return ok


def ingest_drcd(count: int):
    data = json.loads(_gh_fetch(*GH["drcd"]).decode("utf-8"))
    articles = data if isinstance(data, list) else data.get("data", [])
    try:
        from opencc import OpenCC
        cc = OpenCC("t2s")
    except Exception:
        cc = None
    ok = 0
    for article in articles:
        for para in article.get("paragraphs", []):
            if ok >= count:
                break
            text = para["context"]
            if cc:
                text = cc.convert(text)
            if write_doc("百科问答", f"drcd_{ok + 1:03d}.md", article.get("title", "DRCD"), text, "drcd"):
                ok += 1
        if ok >= count:
            break
    print(f"[drcd] 录入 {ok} 篇")
    return ok


def ingest_langchain_local(repo: Path, count: int):
    if not repo.exists():
        print(f"[跳过] 目录不存在: {repo}")
        return 0
    mds = [p for p in repo.rglob("*.md")
           if ".github" not in p.parts and p.name.lower() != "readme_en.md"]
    mds = [p for p in mds if p.stat().st_size >= 500]
    mds.sort(key=lambda p: -p.stat().st_size)
    ok = 0
    for m in mds[:count]:
        text = m.read_text(encoding="utf-8", errors="ignore")
        if write_doc("技术文档", f"langchain_{ok + 1:03d}.md", m.stem, text, "langchain"):
            ok += 1
    print(f"[langchain] 录入 {ok} 篇")
    return ok


def _curl_range(url: str, dest: Path, end: int, start: int = 0, timeout: int = 600):
    r = subprocess.run(["curl.exe", "-sS", "-L", "--ssl-no-revoke", "--max-time", str(timeout),
                        "-r", f"{start}-{end}", "-o", str(dest), url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not dest.exists() or dest.stat().st_size == 0:
        raise RuntimeError(f"下载失败: {url} {r.stderr[:200]}")


def ingest_wiki(count: int):
    """取 fjcanyue/wikipedia-zh-cn 快照（JSONL，纯文本）开头 20MB 内的真实条目。"""
    tmp = Path(sys.path[0]).parent / "data" / "_wiki_chunk.jsonl"
    _curl_range("https://hf-mirror.com/datasets/fjcanyue/wikipedia-zh-cn/resolve/main/wikipedia-zh-cn-20240901.json",
                tmp, end=20 * 1024 * 1024)
    ok = 0
    for line in tmp.read_text(encoding="utf-8", errors="ignore").splitlines():
        if ok >= count:
            break
        try:
            row = json.loads(line)
        except Exception:
            continue
        title = row.get("title") or f"wiki_{ok}"
        text = row.get("text", "")
        if not text:
            continue
        if write_doc("百科", f"wiki_{ok + 1:03d}.md", title, text, "wiki"):
            ok += 1
    tmp.unlink(missing_ok=True)
    print(f"[wiki] 录入 {ok} 篇")
    return ok


THUCNEWS_CATS = ["体育", "娱乐", "家居", "彩票", "房产", "教育", "时尚", "时政", "星座", "游戏", "社会", "科技", "股票", "财经"]


def ingest_thucnews(count: int):
    """从 hf-mirror 的 THUCNews 镜像（Tongjilibo/THUCNews，Apache-2.0）按分类 Range 取数。"""
    base = "https://hf-mirror.com/datasets/Tongjilibo/THUCNews/resolve/main/"
    per = (count + len(THUCNEWS_CATS) - 1) // len(THUCNEWS_CATS)
    ok = 0
    for cat in THUCNEWS_CATS:
        if ok >= count:
            break
        tmp = Path(sys.path[0]).parent / "data" / f"_thucnews_{cat}.jsonl"
        _curl_range(base + urllib.parse.quote(cat) + ".jsonl", tmp, end=2 * 1024 * 1024)
        taken = 0
        for line in tmp.read_text(encoding="utf-8", errors="ignore").splitlines():
            if ok >= count or taken >= per:
                break
            try:
                row = json.loads(line)
            except Exception:
                continue
            title = row.get("title") or f"thucnews_{ok}"
            text = row.get("content") or ""
            if not text:
                continue
            if write_doc("资讯新闻", f"thucnews_{ok + 1:04d}.md", title, text, "thucnews"):
                ok += 1
                taken += 1
        tmp.unlink(missing_ok=True)
    print(f"[thucnews] 录入 {ok} 篇")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cmrc", type=int, default=0)
    ap.add_argument("--drcd", type=int, default=0)
    ap.add_argument("--langchain-dir", type=Path)
    ap.add_argument("--wiki", type=int, default=0)
    ap.add_argument("--thucnews", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    plan = {"cmrc": args.cmrc, "drcd": args.drcd,
            "langchain": 25 if args.langchain_dir else 0,
            "wiki": args.wiki, "thucnews": args.thucnews}
    print(f"[计划] {plan}")
    if args.dry_run:
        return

    total = 0
    if args.cmrc:
        total += ingest_cmrc(args.cmrc)
    if args.drcd:
        total += ingest_drcd(args.drcd)
    if args.langchain_dir:
        total += ingest_langchain_local(args.langchain_dir, 25)
    if args.wiki:
        total += ingest_wiki(args.wiki)
    if args.thucnews:
        total += ingest_thucnews(args.thucnews)
    print(f"\n[完成] 共录入 {total} 篇，来源登记见 data/source_manifest.md")


if __name__ == "__main__":
    main()