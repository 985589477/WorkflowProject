# 最小必要变更治理能力输出

## 已形成的能力

本项目已把 Ponytail 的核心思想融合进 developer-kit，形成“最小必要变更治理”能力。

## 全局资产

| 类型 | 文件 |
| --- | --- |
| 开发子角色 | `02-roles/developer/minimal-change-guardian.md` |
| 工作流 | `04-workflows/developer/minimal-change-governance-workflow.md` |
| 模板 | `06-templates/developer/minimal-change-governance-template.md` |
| 评分表 | `11-evaluations/output-scorecards/minimal-change-governance-scorecard.md` |
| 知识沉淀 | `10-knowledge-base/patterns/ponytail-minimal-change-principles.md` |

## 已增强的全局资产

| 文件 | 增强内容 |
| --- | --- |
| `02-roles/developer/role-definition.md` | 增加最小必要变更职责和子角色 |
| `04-workflows/developer/developer-kit-workflow.md` | 在开发生命周期中加入实现前最小必要变更判断 |
| `04-workflows/developer/implementation-workflow.md` | 加入实现前最小必要变更检查 |
| `04-workflows/developer/code-review-workflow.md` | 加入反过度设计、反不必要依赖和可删除代码检查 |
| `06-templates/developer/implementation-template.md` | 增加最小必要变更判断区块 |
| `11-evaluations/output-scorecards/implementation-scorecard.md` | 增加最小必要变更评分维度 |
| `11-evaluations/output-scorecards/code-review-scorecard.md` | 增加最小必要变更评分维度 |

## 导出包同步

已同步到：

```text
14-exports/developer-kit/
```

## 使用效果

developer-kit 在处理代码任务时，不应直接进入实现，而是先回答：

```text
这件事是否真的需要写代码？
如果要写，最小完整改动是什么？
哪些东西明确不做？
哪些安全、校验、错误处理、可访问性和测试不能省略？
```
