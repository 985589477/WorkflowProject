# 项目记忆摘要

## 一句话定位

跨角色团队总调度能力建设项目，用于协调产品、UI、开发、测试四个角色协作。

## 当前目标

建设 mixed 团队总入口，让用户提出需求后，由总调度判断角色接管顺序、交接状态、验收结果和 badcase 反馈。

## 当前阶段

completed

## 最近一次有效进展

已创建并提升：

- `04-workflows/mixed/team-orchestration-workflow.md`
- `06-templates/mixed/team-orchestration-template.md`
- `11-evaluations/output-scorecards/team-orchestration-scorecard.md`

## 已完成内容

- 已创建 mixed 全局目录。
- 已创建跨角色团队总调度工作流。
- 已创建跨角色团队总调度模板。
- 已创建跨角色团队总调度评分表。
- 已补齐项目 00-06 记录。

## 当前有效决策

| 决策 | 原因 | 影响 | 来源 |
| --- | --- | --- | --- |
| 总调度不替代单角色能力 | 产品、UI、开发、测试已经有各自成熟能力 | mixed 只负责编排、交接、验收和 badcase 反馈 | 本项目 |
| 默认按产品 -> UI -> 开发 -> 测试推进 | 完整项目通常需要先明确需求，再设计，再实现，再验证 | 复杂需求可稳定引导用户往下走 | 用户需求 |
| 下游看不懂上游时必须反馈 | 沟通不畅本身就是能力优化线索 | badcase 可回到对应角色项目优化 | 用户需求 |

## 已废弃方向

| 方向 | 废弃原因 | 替代方案 |
| --- | --- | --- |
| 新建第五个业务角色 | 用户需要的是团队调度，不是替代产品/UI/开发/测试 | 使用 mixed 总调度工作流 |

## 关键风险与注意事项

| 风险 | 影响 | 处理方式 |
| --- | --- | --- |
| 未经过真实完整项目验证 | 调度顺序和交接门禁可能需要微调 | 下一步用真实需求验证 |
| 角色过多导致输出冗长 | 用户可能难以阅读 | 默认只输出当前阶段和下一步，必要时展开 |

## 当前可用资产

| 资产 | 位置 | 用途 |
| --- | --- | --- |
| 团队总调度工作流 | `04-workflows/mixed/team-orchestration-workflow.md` | 组织四角色协作 |
| 团队总调度模板 | `06-templates/mixed/team-orchestration-template.md` | 输出调度计划和交接检查 |
| 团队总调度评分表 | `11-evaluations/output-scorecards/team-orchestration-scorecard.md` | 检查调度质量 |

## 下一步

- 使用真实完整需求验证团队总调度。
- 根据真实 badcase 判断是否拆分跨角色验收工作流或 badcase 复盘工作流。
- 如果团队总调度需要外部独立使用，再建设并导出 `team-kit`。

## 需要追溯时再读

| 文件 | 什么时候读 |
| --- | --- |
| `00-progress/progress-log.md` | 需要查看完整执行流水时。 |
| `00-progress/decision-log.md` | 需要追溯重要决策原因时。 |

