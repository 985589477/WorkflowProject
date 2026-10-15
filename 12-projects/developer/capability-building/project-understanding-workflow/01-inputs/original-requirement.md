# 原始需求

## 用户背景

用户希望建设一套能与 Codex、Cursor 等 AI 开发工具协作的 developer-kit。

当前已经完成：

- 开发治理能力体系。
- 新项目启动治理工作流。

用户接下来需要继续补齐开发治理链路，尤其是让 AI 在进入已有项目时，不只是凭目录猜测，而是能够形成清晰的项目理解、模块边界和后续开发判断。

## 本次建设目标

创建“已有项目理解工作流”，用于：

1. 接手一个已有项目时，指导 AI 应该先阅读哪些文件。
2. 输出项目技术栈、启动方式、目录职责和核心模块。
3. 梳理模块边界、模块协作链路和风险缺口。
4. 为后续需求到架构、模块边界分析、风险评估和实现执行提供上下文。
5. 避免 AI 没理解项目就直接进入代码修改。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/project-understanding-workflow.md
06-templates/developer/project-understanding-template.md
11-evaluations/output-scorecards/project-understanding-scorecard.md
```

同时在项目目录中保留本次能力建设记录：

```text
12-projects/developer/capability-building/project-understanding-workflow/
```

## 约束

- 文档主体使用中文。
- 英文仅保留在路径、命令、文件名和技术名中。
- 不把 WorkflowProject 的内部目录结构强加给外部项目。
- 该工作流是开发治理能力，不是具体代码实现能力。
