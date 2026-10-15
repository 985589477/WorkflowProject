# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够长期协作治理项目，不仅能完成一次开发，还能维护架构决策的可追溯性。

当前已经完成：

- 第一阶段开发前治理链路。
- 第二阶段开发过程治理链路。

下一步进入第三阶段：管住长期维护。

## 本次建设目标

创建“架构决策记录工作流”，用于：

1. 判断是否需要记录 ADR。
2. 记录决策背景。
3. 整理备选方案。
4. 说明选择理由和放弃原因。
5. 分析影响范围和风险代价。
6. 定义复盘条件。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/architecture-decision-record-workflow.md
06-templates/developer/architecture-decision-record-template.md
11-evaluations/output-scorecards/architecture-decision-record-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/architecture-decision-record-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- ADR 不记录普通开发流水账。
- 必须记录备选方案、取舍和复盘条件。
