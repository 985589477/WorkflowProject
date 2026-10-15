# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 不仅能写代码，还能完成可靠的验证和验收闭环。

当前已经完成：

- 开发治理能力体系。
- 第一阶段开发前治理链路。
- 代码实现执行工作流。

下一步需要解决：代码实现完成后，AI 如何根据风险和影响范围进行测试、构建、手动验收、回归检查，并记录未验证内容。

## 本次建设目标

创建“测试与验收工作流”，用于：

1. 明确验证目标。
2. 制定验证计划。
3. 执行自动验证。
4. 输出手动验收步骤。
5. 记录回归范围。
6. 处理验证失败。
7. 记录未验证内容。
8. 给出是否建议交付。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/testing-verification-workflow.md
06-templates/developer/testing-verification-template.md
11-evaluations/output-scorecards/testing-verification-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/testing-verification-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 验证失败不能写成通过。
- 无法验证必须说明原因。
