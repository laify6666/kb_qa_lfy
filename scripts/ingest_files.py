"""一键统一格式入库：把各种格式（Office/PDF/HTML/图片…）统一转成 Markdown 写进 data/raw。

用法（项目根目录）：
  python scripts\ingest_files.py --input <文件或文件夹> [--domain 业务域] [--build]

支持的格式：
  文本:  .md/.markdown/.txt                    -> 直接复制
  图片:  .png/.jpg/.jpeg/.bmp/.webp/.tif/.tiff -> RapidOCR 中文识别（本地离线）
  PDF:   文本型 -> markitdown 抽取；扫描型（抽不出文字）-> PyMuPDF 转图 -> RapidOCR
  Office/Web/数据: .docx/.pptx/.xlsx/.html/.csv/.json/.epub -> markitdown 统一转 Markdown

产物：
  data/raw/<domain>/<原文件名>.md（统一为 Markdown 文本）
  data/source_manifest.md 追加来源登记（来源=本地文件路径）

依赖（已装）：markitdown[docx,pptx,xlsx,pdf]  rapidocr_onnxruntime  pymupdf
"""

import argparse
import sys
import tempfile
from datetime import date
from pathlib import Path

BASE = Path(__file__).parent.parent
RAW_DIR = BASE / "data" / "raw"
MANIFEST = BASE / "data" / "source_manifest.md"
TODAY = date.today().isoformat()

TEXT_EXTS = {".md", ".markdown", ".txt"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".webp", ".tif", ".tiff"}
MARKITDOWN_EXTS = {".docx", ".pptx", ".xlsx", ".html", ".htm", ".csv", ".json", ".epub", ".pdf"}

_md = None
_ocr = None


def _markitdown():
    global _md
    if _md is None:
        from markitdown import MarkItDown
        _md = MarkItDown()
    return _md


def _rapidocr():
    global _ocr
    if _ocr is None:
        from rapidocr_onnxruntime import RapidOCR
        _ocr = RapidOCR()
    return _ocr


def extract_text(path: Path):
    """按扩展名分发，返回 (文本, 说明)。"""
    ext = path.suffix.lower()
    if ext in TEXT_EXTS:
        return path.read_text(encoding="utf-8", errors="ignore"), "文本"
    if ext in IMAGE_EXTS:
        text = _ocr_image(path)
        return text, "图片OCR"
    if ext == ".pdf":
        return _extract_pdf(path), "PDF"
    if ext in MARKITDOWN_EXTS:
        try:
            text = _markitdown().convert(str(path)).text_content or ""
        except Exception as e:
            return "", f"markitdown失败:{str(e)[:60]}"
        return text, "MarkItDown"
    return "", f"不支持的格式:{ext}"


def _ocr_image(path: Path) -> str:
    engine = _rapidocr()
    result, _elapse = engine(str(path))
    if not result:
        return ""
    lines = [str(item[1]) for item in result]
    return "\n".join(lines)


def _extract_pdf(path: Path) -> str:
    try:
        text = _markitdown().convert(str(path)).text_content or ""
    except Exception:
        text = ""
    if len(text.strip()) >= 80:
        return text  # 文本型 PDF
    # 扫描型 PDF：逐页转图 + OCR
    import pymupdf
    pages = []
    with pymupdf.open(str(path)) as doc:
        for page in doc:
            pix = page.get_pixmap(dpi=200)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
                tmp = Path(f.name)
            pix.save(str(tmp))
            pages.append(_ocr_image(tmp))
            tmp.unlink(missing_ok=True)
    return "\n\n".join(p for p in pages if p.strip())


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


def _safe_stem(name: str) -> str:
    for ch in '\\/:*?"<>|':
        name = name.replace(ch, "_")
    return name.strip() or "untitled"


def ingest_one(src: Path, domain: str):
    text, note = extract_text(src)
    if not text.strip():
        print(f"  ⚠️ {src.name} [{note}] 抽取为空，跳过")
        return 0

    d = RAW_DIR / domain
    d.mkdir(parents=True, exist_ok=True)
    stem = _safe_stem(src.stem)
    out = d / f"{stem}.md"
    i = 2
    while out.exists():
        out = d / f"{stem}_{i}.md"
        i += 1

    title = src.stem
    out.write_text(f"# {title}\n\n> 来源：本地文件 `{src}` ｜ 格式：{note}\n\n{text.strip()}", encoding="utf-8")

    n = _next_manifest_no()
    with open(MANIFEST, "a", encoding="utf-8") as f:
        f.write(f"| {n} | data/raw/{domain}/{out.name} | {title} | 本地文件：{src} | {TODAY} | 内部资料（用户提供） |\n")
    print(f"  ✅ {src.name} [{note}] -> {out.name}（{len(text.strip())} 字）")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path, help="文件或文件夹（递归扫描）")
    ap.add_argument("--domain", default="通用", help="业务域（data/raw 下的一级子目录名）")
    ap.add_argument("--build", action="store_true", help="入库后自动增量建库")
    args = ap.parse_args()

    src = args.input.resolve()
    files = sorted(src.rglob("*")) if src.is_dir() else [src]
    files = [f for f in files if f.is_file()]
    print(f"[输入] {src} | 文件数 {len(files)} | 业务域「{args.domain}」")

    ok = skip = 0
    by_type = {}
    for f in files:
        ext = f.suffix.lower()
        if ext not in TEXT_EXTS | IMAGE_EXTS | MARKITDOWN_EXTS:
            print(f"  – {f.name} [不支持的格式 {ext or '(无扩展名)'}]，跳过")
            continue
        by_type[ext] = by_type.get(ext, 0) + 1
        ok += ingest_one(f, args.domain)
    print(f"\n[完成] 入库 {ok} 篇；格式分布 {by_type}；来源已登记 data/source_manifest.md")

    if args.build:
        import subprocess
        subprocess.run([sys.executable, "scripts/build_vectorstore.py", "--incremental"])


if __name__ == "__main__":
    main()