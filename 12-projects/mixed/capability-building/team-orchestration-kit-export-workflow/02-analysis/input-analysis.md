# 输入分析

## 当前已有基础

WorkflowProject 已有跨角色总调度核心资产：

- `04-workflows/mixed/team-orchestration-workflow.md`
- `06-templates/mixed/team-orchestration-template.md`
- `11-evaluations/output-scorecards/team-orchestration-scorecard.md`

这些资产已经能描述产品、UI、开发、测试之间的接管顺序、交接门禁、互审方式和 badcase 反馈规则。

## 导出包需要补齐的内容

仅复制工作流、模板和评分表不够。外部项目还需要：

- `START-HERE.md`：告诉用户和 AI 如何启动。
- `README.md`：解释这个包是什么，不是什么。
- `usage-guide.md`：说明具体怎么用。
- `INSTALL.md`：说明如何放到其他项目。
- `SKILL.md`：作为 Codex skill 草稿。
- `manifest.md`：说明来源和维护方式。
- `examples/quick-start-example.md`：给一个可直接照抄的例子。
- `integrations/codex-usage.md` 和 `integrations/cursor-usage.md`：说明在开发工具里怎么用。

## 命名判断

导出包命名为：

```text
team-orchestration-kit
```

原因：

- 比 `mixed-kit` 更容易理解。
- 明确表达它是团队总调度，不是一个普通混合角色。
- 能与 `product-manager-kit`、`developer-kit` 等并列。

## 使用边界

team-orchestration-kit 只负责总调度，不直接替代四个角色包的专业产出。

如果外部项目没有对应角色包，总调度仍可给出建议，但需要说明缺少角色包带来的影响。
