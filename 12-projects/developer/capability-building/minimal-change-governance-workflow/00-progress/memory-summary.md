# 项目记忆摘要

## 一句话定位

把 Ponytail 的最小必要变更思想融合进 developer-kit。

## 当前目标

形成一个开发角色可调用的“最小必要变更治理”能力，减少 AI 开发中的过度设计和不必要代码。

## 当前阶段

已完成。

## 最近一次有效进展

已完成全局资产建设、导出包同步和项目过程记录。

## 已完成内容

- 下载并阅读 Ponytail 项目核心文件。
- 确认 Ponytail 使用 MIT License。
- 新增开发子角色“最小必要变更守门人”。
- 新增最小必要变更治理工作流、模板、评分表和知识库记录。
- 增强 developer-kit 总入口、实现工作流、代码评审工作流、实现模板和评分表。
- 同步到 `14-exports/developer-kit/`。

## 当前有效决策

| 决策 | 原因 | 影响 | 来源 |
| --- | --- | --- | --- |
| 以子角色方式融合 Ponytail | developer-kit 已有完整治理链路，Ponytail 更适合作为约束能力 | 不替换 developer-kit，只增强实现前和评审时判断 | 用户需求和输入分析 |
| 不为了少写代码牺牲必要质量 | 最小必要变更必须是完整变更 | 安全、校验、错误处理、可访问性和测试不能被省略 | 输出评审 |

## 已废弃方向

| 方向 | 废弃原因 | 替代方案 |
| --- | --- | --- |
| 直接照搬 Ponytail 替代开发角色 | 会削弱当前 developer-kit 的生命周期治理能力 | 融合为开发子角色 |

## 关键风险与注意事项

| 风险 | 影响 | 处理方式 |
| --- | --- | --- |
| 只停留在原则层，没有真实任务验证 | 不确定能否减少实际过度设计 | 后续用真实开发任务验证 |
| AI 误解“少写代码”为省略质量保障 | 可能带来安全和质量风险 | 明确不能省略安全、校验、错误处理、可访问性和测试 |

## 当前可用资产

| 资产 | 位置 | 用途 |
| --- | --- | --- |
| 最小必要变更守门人 | `02-roles/developer/minimal-change-guardian.md` | 开发子角色 |
| 最小必要变更治理工作流 | `04-workflows/developer/minimal-change-governance-workflow.md` | 实现前判断 |
| 最小必要变更模板 | `06-templates/developer/minimal-change-governance-template.md` | 输出结构 |
| 最小必要变更评分表 | `11-evaluations/output-scorecards/minimal-change-governance-scorecard.md` | 质量检查 |
| Ponytail 原则沉淀 | `10-knowledge-base/patterns/ponytail-minimal-change-principles.md` | 知识来源 |

## 下一步

- 使用 developer-kit 跑一次真实代码任务，验证最小必要变更判断是否能减少过度设计。

## 需要追溯时再读

| 文件 | 什么时候读 |
| --- | --- |
| `00-progress/progress-log.md` | 需要查看完整执行流水时。 |
| `00-progress/decision-log.md` | 需要追溯重要决策原因时。 |
