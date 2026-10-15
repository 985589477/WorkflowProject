# 原始需求

## 用户背景

用户正在建设 developer-kit，希望它能与 Codex、Cursor 这类 AI 开发工具协作，用来治理项目开发过程。

当前已经完成：

- 开发治理能力体系。
- 新项目启动治理工作流。
- 已有项目理解工作流。

下一步需要解决：产品需求进入开发之后，AI 如何判断需求会影响当前项目中的哪些模块、接口、数据、状态和风险点。

## 本次建设目标

创建“需求到架构影响分析工作流”，用于：

1. 判断需求是否清楚。
2. 判断需求影响项目哪些区域。
3. 判断是否需要新增模块或调整模块边界。
4. 分析数据、状态、接口和协作影响。
5. 输出风险等级和确认策略。
6. 为后续模块边界、风险评估、影响分析和实现执行提供输入。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/requirement-to-architecture-workflow.md
06-templates/developer/requirement-to-architecture-template.md
11-evaluations/output-scorecards/requirement-to-architecture-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/requirement-to-architecture-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 本工作流不直接写代码。
- 本工作流不替代 PRD，而是把需求转成开发前的架构影响分析。
