# 输入分析

## Ponytail 的核心价值

Ponytail 的核心不是某个工具链，而是一种 AI 编程约束：

```text
最好的代码是没有写出来的代码。
```

它要求 AI 在动手前先判断：

- 这个需求是否真的需要新增代码。
- 是否可以用项目已有能力解决。
- 是否可以用平台能力或标准库解决。
- 是否可以用已安装依赖解决。
- 是否可以用一行清晰代码解决。
- 如果必须新增代码，最小完整实现是什么。

## 与 WorkflowProject 的关系

WorkflowProject 已经有开发治理链路：

```text
需求理解 -> 项目理解 -> 功能规划 -> 风险判断 -> 实现 -> 验证 -> 评审 -> 复盘
```

Ponytail 可以补强其中两个薄弱点：

- 实现前：防止 AI 过早进入写代码模式。
- 评审时：检查是否存在不必要的抽象、依赖、配置、扩展点或文件。

## 不能直接照搬的部分

不能直接把 Ponytail 当作唯一开发角色，因为当前 developer-kit 还需要处理：

- 项目规范检查。
- 模块边界。
- 数据/API/状态契约。
- 安全权限。
- 测试验证。
- 文档同步。
- 发布回滚。

因此本次采用“融合成开发子角色”的方式，而不是替换 developer-kit。

## 融合原则

- 保留 Ponytail 的最小变更思想。
- 用中文重写为可执行的开发治理规则。
- 明确不可为了少写代码而牺牲安全、校验、错误处理、可访问性和测试。
- 让能力进入总入口、实现、评审和导出包。

## 输出形态

本次应形成：

- `02-roles/developer/minimal-change-guardian.md`
- `04-workflows/developer/minimal-change-governance-workflow.md`
- `06-templates/developer/minimal-change-governance-template.md`
- `11-evaluations/output-scorecards/minimal-change-governance-scorecard.md`
- `10-knowledge-base/patterns/ponytail-minimal-change-principles.md`
- developer-kit 导出包同步文件。
