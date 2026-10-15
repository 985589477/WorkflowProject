# 沉淀记录

## 已提升资产

```text
10-knowledge-base/patterns/developer-governance-capability-system.md
```

## 来源项目

```text
12-projects/developer/capability-building/developer-governance-capability-system/
```

## 沉淀原因

用户真正需要的开发角色不是普通代码生成提示词，而是一套让 Codex、Cursor 等 AI 工具能够稳定参与项目开发的治理体系。

该体系需要解决：

- 新项目启动规范。
- 已有项目接手规范。
- 产品需求进入开发后的处理方式。
- 模块边界与模块协作。
- 新增模块判断。
- 变更风险分级。
- 测试、文档、交付和复盘。

## 核心经验

developer-kit 应该是：

```text
开发治理护栏
```

而不是：

```text
固定执行铁轨
```

因此后续所有开发工作流都要保留：

- 任务复杂度判断。
- 小任务轻量执行。
- 项目本地规则优先。
- 高风险任务人工确认。
- AI 可以说明不适合使用完整流程。

## 后续建议

下一步优先建设第一阶段工作流：

```text
project-bootstrap-workflow
project-understanding-workflow
requirement-to-architecture-workflow
module-boundary-analysis-workflow
change-risk-assessment-workflow
impact-analysis-workflow
```

完成后再进入：

```text
implementation-workflow
testing-verification-workflow
documentation-sync-workflow
code-review-workflow
```

## 待验证问题

- 在真实代码项目中，developer-kit 是否会让 AI 更稳，而不是更啰嗦。
- Codex skill 与 Cursor rules 的规则颗粒度是否需要不同。
- 是否需要按前端、后端、全栈、移动端分别细化模块结构。
