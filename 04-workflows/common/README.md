# 通用工作流

这里放跨角色通用工作流。

真实代码项目优先从项目治理主流程开始：

```text
project-governance
-> 检查项目事实和治理缺口
-> 交互式补齐
-> 整体规划和任务列表
-> 按需调用角色能力
-> 逐条执行、验证和同步文档
```

推荐链路：

```text
idea-to-input
-> input-analysis
-> template-generation
-> prompt-generation
-> output-review
-> example-extraction
-> template-iteration
```

## 当前工作流

- `project-governance-workflow.md`：检查真实项目的架构、模块、设计规范、任务列表和模块文档，并在缺失时引导补齐。
- `idea-to-input-workflow.md`：把模糊想法整理成标准输入。
- `input-analysis-workflow.md`：分析标准输入并形成结构化分析。
- `template-generation-workflow.md`：生成可复用模板。
- `prompt-generation-workflow.md`：生成正式提示词。
- `output-review-workflow.md`：评审 AI 输出。
- `example-extraction-workflow.md`：提取优秀案例。
- `template-iteration-workflow.md`：迭代优化模板。
- `project-execution-workflow.md`：总控一次完整项目。
- `iteration-memory-management-workflow.md`：整理长期迭代记录，生成当前项目记忆摘要，降低后续上下文读取成本。
- `asset-promotion-workflow.md`：判断项目产物是否提升为全局资产。
- `capability-export-workflow.md`：把当前项目中的角色能力或专项能力导出为独立能力包。
- `agent-orchestration-workflow.md`：判断直接调用 Skill，或创建父 Agent 与子 Agent。
