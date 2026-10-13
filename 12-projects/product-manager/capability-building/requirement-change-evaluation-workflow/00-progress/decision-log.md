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

## 决策：将需求变更评估作为执行管控能力

### 背景

产品路线图、版本规划、PRD 和开发排期形成后，真实执行中经常出现新增需求、范围调整、优先级变化或需求取消。

### 决策

建设 `requirement-change-evaluation-workflow`，并将它定位为产品经理执行过程中处理需求变化的影响评估机制。

### 原因

没有变更评估机制时，团队容易只凭感觉接受或拒绝变更，导致范围失控、延期、返工或沟通不一致。

### 影响

新增并沉淀以下全局资产：

```text
04-workflows/product-manager/requirement-change-evaluation-workflow.md
06-templates/product-manager/requirement-change-evaluation-template.md
11-evaluations/output-scorecards/requirement-change-evaluation-scorecard.md
```

### 日期

2026-10-13
