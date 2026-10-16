# 导出清单

导出对象：WorkflowProject 统一开发治理能力包
导出时间：2026-10-15T18:35+08:00
导出方式：`python3 tools/export_unified_kit.py`

## 包含能力

- `project-governance-kit/`：项目治理检查
- `team-orchestration-kit/`：跨角色总调度
- `product-manager-kit/`：产品经理能力
- `ui-designer-kit/`：UI 设计能力
- `developer-kit/`：开发治理能力
- `tester-kit/`：测试与验收能力

## 使用边界

- 本包提供 AI 项目治理和角色协作方法，不替代目标项目的真实架构、业务事实和设计决策。
- 总入口负责检查、规划、调度和验收；具体角色能力按需使用。
- 修改源项目中的能力后，应重新运行导出脚本，不直接手工修改本包中的子能力。
