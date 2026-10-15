# 原始需求

## 用户目标

在已经完成开发治理能力体系和 15 个开发工作流之后，需要继续向下推进，把这些能力收束成一个可以在外部项目独立使用的 `developer-kit`。

## 背景

用户希望通过 skill 管理好整个项目开发过程，尤其是在使用 Codex 或 Cursor 时：

- 新项目启动时知道要添加什么规范。
- 产品需求过来后知道如何进入开发链路。
- 能让 AI 理解模块边界、协作方式和风险。
- 能管住实现、测试、文档、评审、发布和复盘。
- 能把角色能力从 WorkflowProject 中拆分出去，给其他项目独立使用。

## 本次建设目标

创建开发治理能力导出包：

```text
14-exports/developer-kit/
```

并保留能力建设项目记录：

```text
12-projects/developer/capability-building/developer-kit-export-workflow/
```

## 输出要求

- 导出包必须有统一入口 `START-HERE.md`。
- 导出包必须有 `README.md`、`usage-guide.md` 和 `manifest.md`。
- 导出包必须包含开发工作流、模板、评分表和开发治理能力总纲。
- 导出包不能复制整个 WorkflowProject。
- 外部项目使用时不能默认输出到 `04-outputs/` 或 `12-projects/`。
- 应支持一句话启动，也支持外部默认读取配置。
