# 输入分析

## 输入是否充足

输入充足。

本项目不是从一句想法开始，而是基于已经完成评审的需求分析结果建设 PRD 生成工作流。

## 关键输入来源

### 需求分析结果

```text
12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/02-analysis/requirement-analysis.md
```

提供了背景、核心问题、目标用户、使用场景、产品目标、范围边界、已知事实、AI 推断和待确认问题。

### 评审扣分点解决方案

```text
12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/02-analysis/review-gap-resolution.md
```

提供了第一版产品定位、用户路径、可量化成功标准、第一版信息架构，以及 PRD 要写和不写的范围。

### 输出评审

```text
12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/05-review/output-review.md
```

提供了需求分析质量判断、PRD 前置风险和必须保留的待确认问题。

## PRD 工作流要解决的问题

需求分析和 PRD 之间需要一个稳定转换层。

如果没有 PRD 工作流，AI 容易出现以下问题：

- 直接把需求分析改写成 PRD，缺少产品结构。
- 忽略待确认问题，把推断写成确定需求。
- 过早写复杂功能，导致第一版范围膨胀。
- 缺少验收标准，开发和测试无法承接。
- 缺少版本边界，MVP 和后续规划混在一起。

## PRD 工作流的设计原则

1. 先确认需求分析是否可以进入 PRD。
2. 不把待确认问题伪装成确定结论。
3. 先写产品目标和范围，再写功能。
4. 每个功能都要能追溯到用户场景或产品目标。
5. PRD 必须包含验收标准。
6. PRD 必须明确本版本不做什么。
7. PRD 输出后必须进入评审。

## 预期产物

本项目应产出：

```text
04-outputs/prd-generation-workflow.md
04-workflows/product-manager/prd-generation-workflow.md
05-review/output-review.md
06-lessons/promotion-notes.md
```
