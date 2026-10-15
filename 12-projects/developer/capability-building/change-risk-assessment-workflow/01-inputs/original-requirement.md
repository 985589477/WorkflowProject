# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够协作管控项目开发，避免项目失控。

当前已经完成：

- 开发治理能力体系。
- 新项目启动治理工作流。
- 已有项目理解工作流。
- 需求到架构影响分析工作流。
- 模块边界分析工作流。

下一步需要解决：AI 在准备修改代码前，如何判断这次变更风险，并决定是否可以直接执行、是否需要方案确认、是否必须人工确认。

## 本次建设目标

创建“变更风险评估工作流”，用于：

1. 判断变更影响对象。
2. 识别风险信号。
3. 将变更分为低风险、中风险、高风险、危险变更。
4. 给出 AI 执行策略。
5. 明确必须人工确认的问题。
6. 明确验证要求和回滚要求。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/change-risk-assessment-workflow.md
06-templates/developer/change-risk-assessment-template.md
11-evaluations/output-scorecards/change-risk-assessment-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/change-risk-assessment-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 高风险和危险变更必须要求人工确认。
- 本工作流不直接写代码。
