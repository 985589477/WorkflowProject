# PRD 工作流建设项目

状态: completed
角色: product-manager
项目类型: capability-building
创建日期: 2026-10-12

## 目标

建设产品经理能力体系中的 PRD 生成工作流。

本项目负责把已经完成的需求分析结果，转换为可复用的 PRD 生成流程，让后续真实项目可以稳定产出 PRD 初稿。

## 项目职责

这个项目负责生成并验证产品经理 PRD 工作流。

它不直接承担某个具体产品的 PRD 长期维护，而是定义后续产品经理如何基于需求分析结果生成 PRD。

## 何时使用

当你要建设、优化或评审产品经理 PRD 生成能力时，使用这个项目。

当你要执行一次具体 PRD 输出任务时，使用本项目沉淀出的全局工作流：

```text
04-workflows/product-manager/prd-generation-workflow.md
```

## 关键产物

- 项目输出：`04-outputs/prd-generation-workflow.md`
- 全局沉淀：`04-workflows/product-manager/prd-generation-workflow.md`
- 测试输入：`12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/`
- 作用定位：产品经理 PRD 生成细分工作流

## 角色

- 产品经理能力体系架构师。
- PRD 工作流架构师。
- 输出质量评审专家。

## 输入材料

输入材料来自已有真实需求分析项目：

```text
12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/
```

重点参考：

```text
02-analysis/requirement-analysis.md
02-analysis/review-gap-resolution.md
05-review/output-review.md
```

## 使用的工作流

- `04-workflows/product-manager/product-manager-workflow.md`
- `04-workflows/product-manager/requirement-analysis-workflow.md`
- `04-workflows/common/asset-promotion-workflow.md`

## 使用的模板

- `06-templates/meta/prompt-generator.md`
- `06-templates/meta/output-reviewer.md`
- 后续可沉淀：`06-templates/product-manager/prd-template.md`

## 当前状态

已完成第一版。

本项目已将 PRD 生成工作流沉淀到：

```text
04-workflows/product-manager/prd-generation-workflow.md
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

已提升：

```text
04-workflows/product-manager/prd-generation-workflow.md
```

已通过真实 PRD 输出项目验证，并沉淀：

```text
06-templates/product-manager/prd-template.md
11-evaluations/output-scorecards/prd-scorecard.md
```
