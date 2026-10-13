# 验证记录

## 验证对象

- `04-workflows/product-manager/prd-generation-workflow.md`

## 验证输入

```text
12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/
```

## 验证结论

PRD 生成工作流可以把需求分析结果转化为结构化 PRD 初稿。

当前工作流能有效控制第一版范围，并能保留不做范围、风险和待确认问题。

## 发现的问题

- PRD 工作流可以生成 PRD，但还缺少专门的 PRD 模板。
- PRD 评审标准可以复用本次评审结构，但还没有全局评分表。
- 如果下一步进入 UI 设计，需要补充页面级信息架构和字段表。

## 建议沉淀

已完成沉淀：

```text
06-templates/product-manager/prd-template.md
11-evaluations/output-scorecards/prd-scorecard.md
```

## 暂不沉淀内容

暂不沉淀 UI 设计工作流。

原因：当前只有产品侧 PRD 和信息架构，还没有真实 UI 设计输入案例。

建议等完成一个 UI 设计输入案例后，再沉淀 UI 设计工作流。
