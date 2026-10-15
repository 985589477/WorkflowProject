# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够在项目开发中完成从需求、架构、边界、风险、实现、验证、文档到评审的闭环。

当前已经完成：

- 第一阶段开发前治理链路。
- 代码实现执行工作流。
- 测试与验收工作流。
- 文档同步工作流。

下一步需要解决：交付前如何对本次代码变更做最终评审，发现 bug、边界问题、漏测、文档不一致和可维护性风险。

## 本次建设目标

创建“代码评审工作流”，用于：

1. 以问题优先的方式评审代码变更。
2. 检查变更范围是否受控。
3. 检查需求符合度和正确性。
4. 检查模块边界和风险控制。
5. 检查测试覆盖和文档一致性。
6. 输出是否建议交付。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/code-review-workflow.md
06-templates/developer/code-review-template.md
11-evaluations/output-scorecards/code-review-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/code-review-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 评审输出必须问题优先。
- 没发现问题时，也要说明测试缺口和剩余风险。
