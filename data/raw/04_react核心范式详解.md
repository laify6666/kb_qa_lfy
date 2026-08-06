# Agent 全面爆发！一文搞懂背后的核心范式 ReAct

> 来源：https://cloud.tencent.cn/developer/article/2608465

## 什么是 ReAct？

ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动态交互完成复杂任务的智能体架构范式。其核心目标是打破传统语言模型"输入-输出"的单向链路，构建"感知-决策-执行-反馈"的智能闭环，使模型从"被动应答者"升级为"主动问题解决者"。

ReAct 具备三个核心特征：

- 显式推理轨迹：模型在执行行动前会生成可追溯的"推理过程"（Thought），清晰说明行动的决策依据，解决了"黑箱决策"的可解释性问题；
- 外部环境锚定：通过调用搜索、计算、数据库查询等外部工具（Act）获取客观反馈（Observe），将推理过程锚定到真实数据，从根源上抑制"事实幻觉"；
- 少量样本泛化：依托 LLM 的上下文学习能力，仅需 1-5 个包含"推理-行动-观察"的完整示例，即可快速适配多场景任务，无需大规模微调。

ReAct 并非单一算法，而是"语言模型+工具集+循环调度机制"的集成架构。

## 核心思想：模拟人类认知的 TAO 闭环

ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 TAO 闭环：

- Thought：模型的"内心独白"，用于分析任务目标、历史反馈和当前状态，明确下一步行动的逻辑依据；
- Act：模型与外部交互的"执行动作"，如调用搜索引擎、计算工具或控制设备；
- Observe：外部环境对行动的"客观反馈"，如搜索结果、计算答案，为下一轮推理提供真实数据支撑。

## 四大设计理念

- 环境锚定原则：强制模型在涉及事实性问题时优先调用外部工具获取证据，禁止仅凭内部知识生成结论。
- 可解释性优先原则：要求推理轨迹必须包含"任务现状-行动目的-预期结果"三个要素，确保人类可追溯决策逻辑。
- 模块解耦原则：将推理逻辑、行动执行、循环调度拆分为独立模块，通过标准化接口通信，仅需替换工具集即可适配不同场景。
- 容错性设计原则：通过异常捕获、行动重试、上下文裁剪等机制处理工具调用失败、格式解析错误等问题。

## ReAct 工作原理

### 初始化阶段

接收自然语言任务目标，明确任务类型与核心约束；输入 1-3 个 Few-shot 示例；创建上下文管理器，存储后续迭代过程中的 TAO 三元组。

### 循环迭代阶段

每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"任务目标+历史 TAO 轨迹"生成推理内容，输出两个关键信息：当前任务进展、下一步行动方案（调用什么工具、参数是什么、预期结果是什么）。
2. Act（行动）：模型将推理结果转化为标准化行动指令，指令必须包含"工具类型"和"参数"，且遵循预定义格式。行动类型包括：信息检索类、数据处理类、服务预订类、结果输出类（finish）。
3. Observe（观察）：行动解析器对标准化指令进行校验，若校验通过则调用对应工具执行；若失败则生成异常反馈。工具执行后，将结果以"结构化、去冗余"的形式返回。
4. 上下文管理器将本轮"推理-行动-观察"三元组追加到历史轨迹中，若轨迹长度超出 LLM 上下文窗口，则通过"保留近期 3 轮+早期摘要"的策略裁剪，随后进入下一轮迭代。

### 终止输出阶段

- 正常终止：模型输出 finish 行动，表明已完成任务目标；
- 超时终止：达到预设最大迭代步数（通常 5-10 步）；
- 异常终止：连续 3 次行动失败，触发熔断机制。

## ReAct 技术架构（三层）

- 核心逻辑层：智能体的"决策大脑"，由"LLM+提示工程模块"构成，包括推理引擎、行动规划器、提示优化模块（温度 0.2-0.3 降低随机性、加入负面示例等）。
- 执行循环层：智能体的"中枢调度"，包括上下文管理器（存储-裁剪-提取历史 TAO 轨迹）、行动解析器（格式校验-参数提取-工具路由）、循环调度器（控制迭代节奏、终止条件判断）。
- 外部交互层：智能体的"手脚与五官"，包括工具集（每个工具需实现统一的 run() 方法，接收标准化参数并返回结构化结果）、交互环境、数据接口。

## ReAct 解决了什么问题？

- 破解"事实幻觉"难题：将推理过程锚定到真实数据。实验数据显示，在 FEVER 事实核查任务中，ReAct 的幻觉率仅为 8.2%，远低于纯思维链（CoT）的 23.5%。
- 破解"策略僵化"难题：在文本游戏 ALFWorld 中，ReAct 仅用 2 个示例即可实现 71% 的任务成功率，远超强化学习模型的 37%。
- 破解"决策不可解释"难题：每一步行动均有明确的逻辑依据，便于人类审计。
- 破解多场景适配的"高成本"难题：核心逻辑层与执行循环层可复用，仅需替换外部交互层的工具与环境即可适配新场景。

## 极简代码框架

```python
class BaseTool:
    """工具基类，定义标准化接口"""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    def run(self, params) -> str:
        raise NotImplementedError("所有工具子类必须实现 run 方法")

class ContextManager:
    """上下文管理器：存储、裁剪与提取历史 TAO 轨迹"""
    def __init__(self, max_length: int = 4000):
        self.max_length = max_length
        self.tao_trajectory = []
    def add_tao(self, thought, action, observation):
        self.tao_trajectory.append({"thought": thought, "action": action, "observation": observation})
        self._prune_trajectory()
    def _prune_trajectory(self):
        # 裁剪超长轨迹：保留近期 3 轮 + 早期摘要
        pass
    def get_context_str(self) -> str:
        return "\n".join([f"步骤{i+1}：思维：{t['thought']} | 行动：{t['action']} | 观察：{t['observation']}" for i, t in enumerate(self.tao_trajectory)])

def react_core_loop(task, tools, llm, max_steps=6):
    """ReAct 核心循环：控制 TAO 迭代流程"""
    context_manager = ContextManager()
    tool_map = {tool.name: tool for tool in tools}
    for step in range(max_steps):
        # 1. 构建提示词，调用 LLM 生成思维与行动
        prompt = build_prompt(task, context_manager.get_context_str(), tool_map)
        llm_output = llm(prompt)
        # 2. 解析思维与行动（真实场景需增加格式校验）
        thought = parse_thought(llm_output)
        action = parse_action(llm_output)
        # 3. 执行行动并获取观察结果
        if action.startswith("finish"):
            return action[len("finish"):-1].strip()
        elif action.startswith(tuple(tool_map.keys())):
            tool_name = next(name for name in tool_map if action.startswith(name))
            observation = tool_map[tool_name].run(action[len(tool_name)+1:-1].strip())
        else:
            observation = f"无效行动：{action}"
        # 4. 更新上下文
        context_manager.add_tao(thought, action, observation)
    return "任务未完成（已达最大步数）"
```

关键点：通过"构建提示词→调用 LLM→解析行动→执行工具→更新上下文"的流程控制 TAO 循环；工具层面替换为专属工具即可落地不同场景。

## ReAct 的局限

ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要"方式压缩信息，容易丢失关键推理逻辑；行动选择完全依赖 LLM 的推理输出，缺乏对行动效果的量化评估，易出现重复调用工具、执行无效行动等冗余问题。其优化方向是与强化学习、外部记忆机制（向量数据库、知识图谱）深度融合。
