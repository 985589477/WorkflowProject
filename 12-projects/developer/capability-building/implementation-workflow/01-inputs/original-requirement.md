# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够在项目开发中完成从理解、分析、风险判断到代码实现的受控协作。

当前第一阶段已经完成：

- 新项目启动治理。
- 已有项目理解。
- 需求到架构影响分析。
- 模块边界分析。
- 变更风险评估。
- 影响范围分析。

下一步进入第二阶段：管住开发过程。

## 本次建设目标

创建“代码实现执行工作流”，用于：

1. 承接已确认的影响范围和风险等级。
2. 在修改前检查工作区状态。
3. 保护用户已有改动。
4. 按最小范围实现代码。
5. 补充测试和文档。
6. 执行验证。
7. 输出实现交付说明。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/implementation-workflow.md
06-templates/developer/implementation-template.md
11-evaluations/output-scorecards/implementation-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/implementation-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 必须保护用户已有改动。
- 必须控制实现范围。
- 必须说明验证结果。
