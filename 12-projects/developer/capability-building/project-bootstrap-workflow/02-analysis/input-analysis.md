# 输入分析

## 工作流定位

`project-bootstrap-workflow` 是 developer-kit 的第一条执行工作流。

它解决的是：

```text
一个新项目刚开始时，AI 应该如何帮用户建立可维护、可协作、可治理的开发基础设施。
```

它不负责直接实现业务需求，也不负责替代框架脚手架工具。

## 为什么优先建设

如果新项目没有基础规范，后续 AI 开发容易出现：

- 不知道项目目标。
- 不知道项目启动方式。
- 不知道测试和构建命令。
- 不知道目录边界。
- 不知道哪些操作危险。
- 不知道模块应该怎么拆。
- 不知道交付后要同步哪些文档。
- Codex / Cursor 各自按不同规则工作。

因此新项目启动治理是 developer-kit 的前置能力。

## 工作流应该输出什么

该工作流不应该直接“生成一堆复杂文档”，而应该先检查、再建议、再按用户确认补齐。

建议输出：

- 项目启动检查报告。
- 缺失规范清单。
- 建议补齐文件。
- AI 协作规则草案。
- 开发规范草案。
- 质量检查清单。
- 后续开发建议。

## 需要避免的问题

- 不要不看项目就创建固定目录。
- 不要强行覆盖已有 README、AGENTS.md 或 Cursor rules。
- 不要把 WorkflowProject 内部目录结构强加给外部项目。
- 不要为简单项目创建过重的治理结构。
- 不要把所有文件都直接写入，除非用户明确允许。

## 推荐基础文件

最低建议：

```text
README.md
AGENTS.md
docs/development-standard.md
docs/quality-checklist.md
docs/architecture/README.md
```

可选补充：

```text
.cursor/rules/developer-kit.mdc
docs/architecture/module-map.md
docs/architecture/module-contract-template.md
docs/decisions/
docs/release-checklist.md
```
