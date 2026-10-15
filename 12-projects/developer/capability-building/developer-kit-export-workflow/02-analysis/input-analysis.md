# 输入分析

## 问题判断

当前问题不是继续新增单个开发工作流，而是把已经完成的开发治理能力整合成可使用、可复制、可维护的能力包。

如果只保留 `04-workflows/developer/`，它适合在 WorkflowProject 内部维护，但外部项目使用成本较高。

如果直接复制整个 WorkflowProject，外部项目会被大量无关目录干扰。

因此需要一个独立导出层：

```text
14-exports/developer-kit/
```

## 能力包边界

developer-kit 应包含：

- 开发角色工作流。
- 开发角色模板。
- 开发角色评分表。
- 开发治理能力总纲。
- 外部项目启动入口。
- 输出目录规则。
- 自动读取配置示例。

developer-kit 不应包含：

- 具体能力建设项目过程材料。
- XMind 导图。
- React dashboard。
- WorkflowProject 内部目录约定。
- 其他角色能力包。

## 外部使用关键点

外部项目使用 developer-kit 时，最重要的不是让 AI 多读文档，而是让 AI 快速判断：

1. 当前任务属于哪类开发任务。
2. 是否需要完整治理流程。
3. 应使用哪个工作流。
4. 是否可以直接实现。
5. 输出应保存在哪里。
6. 如何验证和复盘。

## 风险

| 风险 | 说明 | 处理方式 |
| --- | --- | --- |
| 包太重 | AI 读取太多文件会增加成本 | 入口先判断任务，再按需读取 |
| 包太轻 | 只给启动话术，无法稳定执行 | 同步导出 workflow、template、scorecard |
| 限制 AI 能力 | 文档变成死流程 | 明确小任务轻量执行，大任务完整治理 |
| 外部目录污染 | 在外部项目创建 WorkflowProject 内部目录 | 明确输出目录策略 |

## 推荐方案

采用与 `product-manager-kit` 一致的导出包结构，并新增开发侧执行规则：

```text
developer-kit/
├── START-HERE.md
├── README.md
├── usage-guide.md
├── manifest.md
├── SKILL.md
├── workflows/
├── templates/
├── scorecards/
├── knowledge/
└── examples/
```
