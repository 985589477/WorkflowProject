# 沉淀记录

## 已提升资产

```text
04-workflows/developer/project-bootstrap-workflow.md
06-templates/developer/project-bootstrap-template.md
11-evaluations/output-scorecards/project-bootstrap-scorecard.md
```

## 来源项目

```text
12-projects/developer/capability-building/project-bootstrap-workflow/
```

## 沉淀原因

新项目启动治理是 developer-kit 的第一条关键工作流。

如果新项目缺少 README、AGENTS.md、docs、开发规范、质量检查清单、测试和构建说明，后续 Codex / Cursor 协作时会缺少边界，容易造成项目失控。

## 核心经验

新项目启动治理不能直接创建一堆固定文件。

正确方式是：

```text
先检查现状
再判断复杂度
再列缺失项
再给补齐方案
最后经用户确认后创建或修改文件
```

## 后续建议

下一步建议建设：

```text
project-understanding-workflow
```

用于已有项目接手时，帮助 AI 快速理解项目结构、技术栈、启动方式、测试方式、主要模块和潜在风险。

## 待验证问题

- 在真实新项目中，是否会补太多文件。
- Cursor rules 与 AGENTS.md 是否需要不同颗粒度。
- 是否需要按前端、后端、全栈生成不同启动治理模板。
