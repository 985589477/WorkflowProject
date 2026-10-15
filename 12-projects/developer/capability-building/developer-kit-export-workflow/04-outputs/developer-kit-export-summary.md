# developer-kit 导出结果

## 导出位置

```text
14-exports/developer-kit/
```

## 已导出内容

| 类型 | 位置 | 说明 |
| --- | --- | --- |
| 启动入口 | `START-HERE.md` | 外部项目优先阅读文件 |
| 使用说明 | `usage-guide.md` | 告诉用户如何选择工作流 |
| 来源清单 | `manifest.md` | 记录导出时间、来源和维护方式 |
| Skill 草稿 | `SKILL.md` | 可用于后续沉淀为 Codex skill |
| 接入说明 | `INSTALL.md` | 外部项目首次接入和验证说明 |
| 总入口工作流 | `workflows/developer/developer-kit-workflow.md` | 开发任务判断和调度入口 |
| 工作流 | `workflows/developer/` | 19 个开发治理细分工作流，加 1 个总入口工作流 |
| 模板 | `templates/developer/` | 开发治理模板 |
| 评分表 | `scorecards/` | 开发治理评分表 |
| 知识总纲 | `knowledge/developer-governance-capability-system.md` | 开发治理能力体系 |
| 示例区 | `examples/quick-start-example.md` | 快速启动示例 |
| 工具集成 | `integrations/` | Codex 和 Cursor 使用说明 |

## 一句话使用方式

```text
请使用 developer-kit 协助我处理这个开发任务：{写下你的任务}
```

## 总入口升级

`developer-kit-workflow.md` 已从“任务分流器”升级为“开发治理主流程”。

它不再把命中某个细分工作流作为结束，而是要求每一步判断后续阶段：

```text
需求理解
-> 是否确认进入开发
-> 项目理解
-> 功能整体规划
-> 风险和影响范围确认
-> 代码实现
-> 测试验证
-> 文档同步
-> 代码评审
-> 发布或复盘判断
```

进入实现前必须先形成整体功能规划。

遇到目标、范围、方案、验收或风险不明确时，应主动询问用户。

## 推荐自动读取配置

外部项目可以在根目录增加：

```text
AI-WORKFLOW-RULES.md
```

并把 `developer-kit/START-HERE.md` 中“外部自动读取配置”的内容复制进去。

这样用户不必每次都输入“请使用 developer-kit”，AI 可以根据任务意图自动判断是否调用。

## 输出目录规则

在外部项目中保存文档时：

1. 用户指定目录优先。
2. 已有文档目录优先。
3. 已有开发文档目录优先。
4. 没有合适目录时创建 `docs/`。

不默认创建：

```text
04-outputs/
12-projects/
```

## 结论

developer-kit 已具备离开 WorkflowProject 独立使用的基础条件。

下一步可以选择：

- 在另一个真实代码项目里验证 developer-kit。
- 将 `14-exports/developer-kit/SKILL.md` 安装为本机 Codex skill。
- 为 Cursor 增加专门的 rules 文件。

## 使用体验补齐

本次补齐后，developer-kit 在真实外部项目中的使用链路更完整：

1. `INSTALL.md` 解决第一次接入问题。
2. `examples/quick-start-example.md` 解决用户不知道 AI 应该如何启动的问题。
3. `integrations/codex-usage.md` 说明 Codex 使用方式。
4. `integrations/cursor-usage.md` 说明 Cursor 使用方式。
5. `START-HERE.md` 增加执行状态格式和任务结束标准。

## 实现阶段增强

developer-kit 已补充“开发任务拆解与逐条执行”能力。

中高风险实现必须先输出开发任务列表：

```text
序号 / 任务 / 目标 / 影响文件或模块 / 前置依赖 / 验收标准 / 验证方式 / 状态
```

执行时必须：

```text
一次只执行一条任务 -> 验证本条任务 -> 记录结果 -> 判断是否进入下一条
```

## 开发前规范检查增强

developer-kit 已补充“开发前规范检查门禁”。

进入代码实现前，AI 必须先检查并说明项目是否存在：

- 设计规范、组件规范、交互规范、视觉规范。
- 代码风格、架构约束、目录约定、命名规范。
- 测试规范、文档规范。
- AI 协作规则，例如 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`.cursor/rules/`。

如果项目已有规范，必须先阅读并遵守；如果没有找到规范，需要说明缺失项，并根据风险决定是从现有代码归纳临时约定、先补充最小规范，还是向用户确认。

## 真实开发协同能力补齐

developer-kit 已补充 4 个细分能力：

| 能力 | 文件 | 作用 |
| --- | --- | --- |
| 问题定位 | `issue-diagnosis-workflow.md` | 报错、白屏、测试失败、性能异常时先复现和定位根因。 |
| 数据/API/状态契约 | `data-api-contract-workflow.md` | 明确字段、接口、状态归属、错误处理和兼容策略。 |
| 安全与权限治理 | `security-permission-workflow.md` | 处理登录、鉴权、角色权限、敏感数据、密钥、上传下载和支付风险。 |
| 工作流协同编排 | `workflow-orchestration-guide.md` | 管理多个工作流之间的插入、回退、跳过和暂停确认。 |
