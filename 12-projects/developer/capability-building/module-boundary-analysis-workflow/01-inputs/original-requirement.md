# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够更好地协作管控项目开发。

当前已经完成：

- 开发治理能力体系。
- 新项目启动治理工作流。
- 已有项目理解工作流。
- 需求到架构影响分析工作流。

下一步需要解决：当需求影响多个模块、职责不清或可能需要新增模块时，AI 如何判断代码应该放在哪里，以及模块之间如何协作。

## 本次建设目标

创建“模块边界分析工作流”，用于：

1. 判断能力点归属哪个模块。
2. 判断是否应该新增模块。
3. 明确模块负责什么、不负责什么。
4. 明确模块输入、输出、依赖和禁止依赖。
5. 明确数据和状态归属。
6. 输出模块协作方式和边界风险。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/module-boundary-analysis-workflow.md
06-templates/developer/module-boundary-analysis-template.md
11-evaluations/output-scorecards/module-boundary-analysis-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/module-boundary-analysis-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 本工作流不直接写代码。
- 新增模块必须有清晰判断依据。
