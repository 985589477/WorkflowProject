# 跨角色团队总调度导出包输出

## 已创建导出包

```text
14-exports/team-orchestration-kit/
```

## 包含内容

| 类型 | 文件 |
| --- | --- |
| 入口 | `START-HERE.md` |
| 说明 | `README.md` |
| 使用指南 | `usage-guide.md` |
| 安装说明 | `INSTALL.md` |
| Codex skill 草稿 | `SKILL.md` |
| 来源清单 | `manifest.md` |
| 工作流 | `workflows/mixed/team-orchestration-workflow.md` |
| 模板 | `templates/mixed/team-orchestration-template.md` |
| 评分表 | `scorecards/team-orchestration-scorecard.md` |
| 长期记忆工作流 | `workflows/common/iteration-memory-management-workflow.md` |
| 长期记忆模板 | `templates/common/iteration-memory-summary-template.md` |
| 示例 | `examples/quick-start-example.md` |
| 工具说明 | `integrations/codex-usage.md`、`integrations/cursor-usage.md` |

## 使用方式

推荐把它与四个角色包同级放置：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```

然后对 AI 说：

```text
请使用 team-orchestration-kit 调度产品、UI、开发和测试处理我的任务：{任务}
```

## 关键设计

- 总调度包只负责跨角色判断、交接检查、互审和验收，不替代单个角色包。
- 如果任务只属于单一角色，应建议直接使用对应角色包。
- 如果交接不通过，应停止推进，输出阻塞和 badcase 回流建议。
