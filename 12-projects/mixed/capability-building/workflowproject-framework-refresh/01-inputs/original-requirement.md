# 原始需求

## 用户想法

用户询问在新增能力导出层和完成产品经理能力体系后，是否需要重新跑一次 `workflowproject-framework-bootstrap`。

进一步确认后，用户接受创建新的 `workflowproject-framework-refresh`，并将旧的 `workflowproject-framework-bootstrap` 降级为历史档案。

## 背景

最初的 `workflowproject-framework-bootstrap` 负责从 0 到 1 搭建项目框架。

但当前 WorkflowProject 已新增或完善：

- `13-visual-maps/`：XMind 和 Markdown 导图。
- `14-exports/`：独立能力包导出区。
- `15-dashboard/`：React 可视化控制台。
- `workflowproject-executor`：本地 Codex skill。
- 产品经理完整能力体系。
- 能力导出工作流。

因此旧 bootstrap 不应继续作为当前框架说明。

## 目标

创建一个新的框架刷新项目，作为当前 WorkflowProject 的最新架构快照和同步记录。

## 预期结果

- 当前框架说明完成同步。
- 旧 bootstrap 项目归档。
- 项目索引、XMind 和 dashboard 刷新。
