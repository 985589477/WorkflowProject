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

## 决策：将版本复盘作为产品经理主链路收尾能力

### 背景

产品经理能力体系已经覆盖从想法、需求分析、PRD、规划、路线图到需求变更评估的过程，但还缺少版本结束后的复盘能力。

### 决策

建设 `version-retrospective-workflow`，并将它定位为版本完成、上线或阶段结束后的复盘和改进机制。

### 原因

版本复盘可以把目标达成、需求交付、变更影响、质量问题、协作问题和后续动作沉淀下来，并回流到需求池、路线图、下一轮版本规划或流程改进。

### 影响

新增并沉淀以下全局资产：

```text
04-workflows/product-manager/version-retrospective-workflow.md
06-templates/product-manager/version-retrospective-template.md
11-evaluations/output-scorecards/version-retrospective-scorecard.md
```

产品经理主链路从“想法输入”到“版本复盘”形成闭环。

### 日期

2026-10-13
