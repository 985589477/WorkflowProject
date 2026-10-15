# AI 提示词模板工具需求分析项目

状态: completed
角色: product-manager
项目类型: real-cases
创建日期: 2026-10-12

## 目标

使用产品经理需求分析工作流，把一个模糊产品想法整理成结构化需求分析结果。

本项目同时用于验证：

- `04-workflows/product-manager/requirement-analysis-workflow.md`
- `06-templates/product-manager/requirement-analysis-template.md`
- `11-evaluations/output-scorecards/requirement-analysis-scorecard.md`

## 项目职责

这个项目负责验证“需求分析工作流”是否能把一句话产品想法变成可进入 PRD 的需求分析。

它不是模板建设项目，而是一次真实使用案例。

## 何时使用

当你想参考“如何用需求分析工作流处理一个模糊产品想法”时，使用这个项目。

当你想继续把 AI 提示词模板工具推进到 PRD、功能规划或界面设计时，也可以从这个项目继续。

## 关键产物

- 标准输入：`01-inputs/original-requirement.md`
- 需求分析：`02-analysis/requirement-analysis.md`
- 扣分点解决方案：`02-analysis/review-gap-resolution.md`
- 输出评审：`05-review/output-review.md`
- 验证记录：`06-lessons/validation-notes.md`

## 角色

- 产品经理。
- 需求分析评审者。
- 工作流验证者。

## 输入材料

输入材料来自一个真实但仍然模糊的产品想法：

```text
我想做一个管理 AI 提示词模板的工具，可以保存、分类、复用和优化提示词。
```

具体材料放在：

```text
01-inputs/original-requirement.md
```

## 使用的工作流

- `04-workflows/product-manager/requirement-analysis-workflow.md`

## 使用的模板

- `06-templates/product-manager/requirement-analysis-template.md`

## 当前状态

已完成第一轮需求分析与评审。

核心输出：

```text
02-analysis/requirement-analysis.md
05-review/output-review.md
```

评审结论：

```text
可以进入 PRD 初稿，但必须保留并确认关键问题。
```

## 如何启动

下次继续本项目时，先阅读：

```text
README.md
00-progress/memory-summary.md
00-progress/next-actions.md
```

然后对 AI 说：

```text
请继续推进这个项目，并先说明当前状态、推荐下一步和会使用哪些文件。
```

## 进度记录

关键执行节点记录到：

```text
00-progress/progress-log.md
```

## 沉淀与提升

本项目用于证明需求分析工作流可以处理一句话产品想法，并能输出可继续进入 PRD 的结构化分析。

后续如果继续推进，可以创建 PRD 项目，或把本案例沉淀到：

```text
09-examples/product-manager/
```
