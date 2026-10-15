# 项目记忆摘要

## 一句话定位

本项目负责把 WorkflowProject 中的开发治理能力整理并导出为可在外部项目独立使用的 `developer-kit`。

## 当前目标

让 `developer-kit` 能作为 Codex、Cursor 等 AI 开发工具的协作治理能力包使用，覆盖从项目理解、需求转开发、模块边界、风险控制、实现、测试、文档、评审、发布到复盘的完整开发链路。

## 当前阶段

已完成第一版导出，并持续增强真实开发协同能力。

## 最近一次有效进展

- 增强了开发前规范检查门禁。
- 增强了开发任务拆解与逐条执行机制。
- 新增了问题定位、数据/API/状态契约、安全与权限治理、工作流协同编排 4 个细分能力。
- 新增了迭代记忆管理机制，用于减少长期项目历史读取成本。
- 2026-10-14 已将迭代记忆管理落地到已有项目和导出包。

## 已完成内容

- 已导出 `14-exports/developer-kit/`。
- 已补齐 `START-HERE.md`、`README.md`、`usage-guide.md`、`INSTALL.md`、`SKILL.md`、`manifest.md`。
- 已补齐 Codex 和 Cursor 使用说明。
- 已同步开发工作流、模板、评分表和知识总纲。
- 已将 developer 总入口升级为生命周期编排器。

## 当前有效决策

| 决策 | 原因 | 影响 | 来源 |
| --- | --- | --- | --- |
| developer-kit 总入口必须是生命周期编排器 | 单点分流无法支撑真实开发闭环 | 总入口需要持续判断下一阶段 | `developer-kit-workflow.md` |
| 进入实现前必须做整体规划 | 避免 AI 直接局部改代码导致边界失控 | 实现前必须说明范围、影响、顺序、验证 | `implementation-workflow.md` |
| 中高风险实现前必须拆任务 | 降低一次性大范围修改风险 | 实现必须逐条执行、逐条验证 | `implementation-workflow.md` |
| 进入实现前必须检查项目规范 | 避免代码风格、组件规范和协作规则不一致 | AI 需要先找设计、开发、测试、AI 协作规则 | `developer-kit-workflow.md` |
| 报错和测试失败先定位再修复 | 根因不清时直接修改容易扩大问题 | 新增 `issue-diagnosis-workflow.md` | `issue-diagnosis-workflow.md` |
| 数据/API/状态要先定义契约 | 避免字段、状态、接口随手改 | 新增 `data-api-contract-workflow.md` | `data-api-contract-workflow.md` |
| 权限和敏感数据先做治理 | 安全相关任务不能靠普通实现兜底 | 新增 `security-permission-workflow.md` | `security-permission-workflow.md` |

## 已废弃方向

| 方向 | 废弃原因 | 替代方案 |
| --- | --- | --- |
| 只做简单工作流分流 | 无法支撑完整开发链路 | 使用生命周期编排 |
| 让 AI 每次读取全部历史 | token 成本高，且历史信息噪声大 | 使用 `memory-summary.md` 管理当前记忆 |

## 关键风险与注意事项

| 风险 | 影响 | 处理方式 |
| --- | --- | --- |
| 文档能力写得完整但未经过真实项目验证 | 外部使用体验可能仍有盲区 | 下一步应拿真实代码项目验证 |
| 细分工作流越来越多导致用户不知道选哪个 | 使用成本上升 | 总入口负责调度，用户优先使用 `developer-kit-workflow.md` |
| 长期迭代记录堆积 | AI 每次读取历史成本过高 | 使用 `iteration-memory-standard.md` 和 `memory-summary.md` |

## 当前可用资产

| 资产 | 位置 | 用途 |
| --- | --- | --- |
| developer-kit 导出包 | `14-exports/developer-kit/` | 外部项目使用 |
| 开发治理总入口 | `04-workflows/developer/developer-kit-workflow.md` | 调度开发任务 |
| 开发治理能力总纲 | `10-knowledge-base/patterns/developer-governance-capability-system.md` | 理解能力地图 |
| 角色能力包生命周期标准 | `05-standards/role-kit-lifecycle-standard.md` | 统一角色包建设 |
| 迭代记忆管理标准 | `05-standards/iteration-memory-standard.md` | 管理长期项目历史 |

## 下一步

- 使用真实代码项目验证 `developer-kit`。
- 验证过程中观察总入口是否能正确插入问题定位、契约治理、安全权限治理和规范检查。
- 如果真实项目中仍出现历史读取负担，继续优化 `memory-summary.md` 的字段和更新规则。
- 后续导出其他角色能力包时，必须同时检查是否携带迭代记忆管理说明。

## 需要追溯时再读

| 文件 | 什么时候读 |
| --- | --- |
| `00-progress/progress-log.md` | 需要查看完整建设过程时。 |
| `00-progress/decision-log.md` | 需要追溯某个能力建设决策时。 |
| `04-outputs/developer-kit-export-summary.md` | 需要查看导出包整体结果时。 |
| `06-lessons/promotion-notes.md` | 需要查看沉淀经验时。 |
