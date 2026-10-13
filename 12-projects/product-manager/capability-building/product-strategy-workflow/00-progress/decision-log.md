# 决策记录

## 使用说明

这里记录项目执行过程中重要决策的原因。

进度记录回答“做到了哪一步”，决策记录回答“为什么这么做”。

## 记录模板

```md
## 决策：{决策标题}

### 背景

为什么出现这个问题？

### 决策

最终决定做什么？

### 原因

为什么这样做？

### 影响

这个决策会影响哪些文件、流程或后续方向？

### 日期

YYYY-MM-DD
```

## 决策：将产品策略判断作为需求池管理前置能力

### 背景

产品经理能力体系已经覆盖需求分析、PRD、验收标准、功能规划、用户故事、用户反馈、竞品分析、优先级判断和版本规划，但还缺少判断产品方向是否成立的上层能力。

### 决策

建设 `product-strategy-workflow`，并将它定位为需求分析、优先级判断、版本规划和产品路线图之前的策略入口。

### 原因

如果没有产品策略判断，后续工作流容易只回答“怎么做”，无法稳定回答“为什么做、是否现在做、服务谁、成功标准是什么”。

### 影响

新增并沉淀以下全局资产：

```text
04-workflows/product-manager/product-strategy-workflow.md
06-templates/product-manager/product-strategy-template.md
11-evaluations/output-scorecards/product-strategy-scorecard.md
```

### 日期

2026-10-12
