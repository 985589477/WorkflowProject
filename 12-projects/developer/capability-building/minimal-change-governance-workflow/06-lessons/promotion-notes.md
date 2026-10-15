# 沉淀记录

## 是否沉淀

已沉淀。

## 沉淀到哪里

- `02-roles/developer/minimal-change-guardian.md`
- `04-workflows/developer/minimal-change-governance-workflow.md`
- `06-templates/developer/minimal-change-governance-template.md`
- `11-evaluations/output-scorecards/minimal-change-governance-scorecard.md`
- `10-knowledge-base/patterns/ponytail-minimal-change-principles.md`
- `14-exports/developer-kit/`

## 沉淀原因

开发型 AI 很容易在实现中出现：

- 写太多代码。
- 抽象过早。
- 新增不必要依赖。
- 创建不必要配置和扩展点。
- 没有先复用项目已有能力。

这类问题会让项目后续维护成本上升，因此需要成为开发角色的基础治理能力。

## 与 Ponytail 的关系

Ponytail 提供了关键思想来源。

本项目没有把 Ponytail 作为独立运行依赖，而是将其核心原则融合为 WorkflowProject 的中文角色能力。

## 后续验证方式

在真实开发任务中检查：

- 实现前是否输出最小必要变更判断。
- 是否减少不必要代码和文件。
- 是否仍保留安全、校验、错误处理、可访问性和测试。
- 代码评审是否能识别过度设计。
