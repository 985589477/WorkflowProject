# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够在项目开发中先建立结构、边界、风险和影响范围，再进入实现。

当前已经完成：

- 开发治理能力体系。
- 新项目启动治理工作流。
- 已有项目理解工作流。
- 需求到架构影响分析工作流。
- 模块边界分析工作流。
- 变更风险评估工作流。

下一步需要解决：风险可控后，AI 如何把变更拆成具体的文件、接口、数据、测试和文档影响清单。

## 本次建设目标

创建“影响范围分析工作流”，用于：

1. 明确变更边界。
2. 列出确定影响文件。
3. 列出可能影响文件。
4. 标明无需修改区域。
5. 梳理调用链。
6. 分析接口、数据、状态、配置影响。
7. 分析测试和文档同步影响。
8. 给出建议实现顺序。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/impact-analysis-workflow.md
06-templates/developer/impact-analysis-template.md
11-evaluations/output-scorecards/impact-analysis-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/impact-analysis-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 本工作流不直接写代码。
- 必须区分确定影响、可能影响、无需修改和待确认。
