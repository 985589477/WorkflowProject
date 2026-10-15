# AI 提示词模板工具 PRD 项目

状态: completed
角色: product-manager
项目类型: real-cases
创建日期: 2026-10-12

## 目标

使用 PRD 生成工作流，把已有需求分析结果转化为 AI 协作资产导航层的 PRD 初稿。

## 项目职责

这个项目负责验证 `04-workflows/product-manager/prd-generation-workflow.md` 是否能从需求分析结果生成可用 PRD。

它不是 PRD 工作流建设项目，而是一次真实 PRD 输出案例。

## 何时使用

当你想参考“如何从需求分析生成 PRD”时，使用这个项目。

当你想继续推进 AI 协作资产导航层的 UI 设计、开发拆解或验收标准时，也可以从这个项目继续。

## 关键产物

- 输入材料：`01-inputs/original-requirement.md`
- PRD 就绪判断：`02-analysis/prd-readiness.md`
- PRD 范围：`02-analysis/prd-scope.md`
- 用户场景：`02-analysis/prd-user-scenarios.md`
- 功能清单：`02-analysis/feature-list.md`
- 功能说明：`04-outputs/feature-spec.md`
- 验收标准：`04-outputs/acceptance-criteria.md`
- PRD 初稿：`04-outputs/prd.md`
- PRD 评审：`05-review/prd-review.md`

## 角色

- 产品经理。
- PRD 评审者。
- 工作流验证者。

## 输入材料

输入来自需求分析项目：

```text
12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/
```

## 使用的工作流

- `04-workflows/product-manager/prd-generation-workflow.md`

## 使用的模板

- `12-projects/product-manager/capability-building/prd-workflow/03-prompts/final-prompt.md`

## 当前状态

已完成第一轮 PRD 生成与评审。

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

## 沉淀与提升

本项目已验证 PRD 工作流，并已反向沉淀：

```text
06-templates/product-manager/prd-template.md
11-evaluations/output-scorecards/prd-scorecard.md
```
