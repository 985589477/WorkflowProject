# 验收标准工作流建设项目

状态: completed
角色: product-manager
项目类型: capability-building
创建日期: 2026-10-12

## 目标

建设产品经理能力体系中的验收标准生成工作流。

本项目负责把 PRD、功能说明和功能清单转化为可验证的验收标准，让产品、设计、开发和测试对“什么算完成”形成一致理解。

## 项目职责

这个项目负责生成并验证产品经理验收标准工作流。

它不直接长期维护某个具体产品的验收标准，而是定义后续产品经理如何从 PRD 生成验收标准。

## 何时使用

当你要建设、优化或评审验收标准生成能力时，使用这个项目。

当你要执行一次具体验收标准输出任务时，使用本项目沉淀出的全局工作流：

```text
04-workflows/product-manager/acceptance-criteria-workflow.md
```

## 关键产物

- 项目输出：`04-outputs/acceptance-criteria-workflow.md`
- 全局沉淀：`04-workflows/product-manager/acceptance-criteria-workflow.md`
- 全局模板：`06-templates/product-manager/acceptance-criteria-template.md`
- 全局评分表：`11-evaluations/output-scorecards/acceptance-criteria-scorecard.md`
- 测试输入：`12-projects/product-manager/real-cases/ai-template-tool-prd/`

## 角色

- 产品经理能力体系架构师。
- 验收标准工作流架构师。
- 输出质量评审专家。

## 输入材料

输入材料来自已有真实 PRD 项目：

```text
12-projects/product-manager/real-cases/ai-template-tool-prd/
```

重点参考：

```text
04-outputs/prd.md
04-outputs/feature-spec.md
04-outputs/acceptance-criteria.md
05-review/prd-review.md
```

## 使用的工作流

- `04-workflows/product-manager/prd-generation-workflow.md`
- `04-workflows/common/asset-promotion-workflow.md`

## 使用的模板

- `06-templates/product-manager/prd-template.md`
- `06-templates/meta/output-reviewer.md`

## 当前状态

已完成第一版。

本项目已将验收标准工作流、模板和评分表沉淀到全局目录。

## 如何启动

下次继续本项目时，先阅读：

```text
README.md
00-progress/next-actions.md
00-progress/progress-log.md
```

然后对 AI 说：

```text
请继续推进这个项目，并先说明当前状态、推荐下一步和会使用哪些文件。
```

## 沉淀与提升

已提升：

```text
04-workflows/product-manager/acceptance-criteria-workflow.md
06-templates/product-manager/acceptance-criteria-template.md
11-evaluations/output-scorecards/acceptance-criteria-scorecard.md
```
