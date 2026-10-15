# 决策记录

## 2026-10-14：导出包命名为 team-orchestration-kit

原因：

- `mixed-kit` 对外部使用者不够直观。
- `team-orchestration-kit` 能明确表达“团队总调度”的职责。

影响：

- 外部使用时建议与 `product-manager-kit`、`ui-designer-kit`、`developer-kit`、`tester-kit` 同级放置。

## 2026-10-14：总调度不替代四个角色包

原因：

- 产品、UI、开发、测试各自已有专业能力包。
- 总调度的职责是判断角色、控制交接、推动验收和反馈 badcase。

影响：

- `team-orchestration-kit` 需要明确说明依赖关系。
- 如果缺少某个角色包，需要说明影响并降级为调度建议。
