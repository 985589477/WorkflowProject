# 下一步判断

## 使用说明

这里用于帮助用户判断项目下一步该往哪里走。

## 当前项目状态

已完成第一版。

本项目已沉淀：

```text
04-workflows/developer/project-bootstrap-workflow.md
06-templates/developer/project-bootstrap-template.md
11-evaluations/output-scorecards/project-bootstrap-scorecard.md
```

## 可选方向

### 方向 A：继续推进当前项目

- 价值：可以继续用真实新项目验证启动治理文件是否足够轻量。
- 风险：如果继续在本项目内过度细化，可能提前绑定某个技术栈。
- 建议：先进入下一条工作流建设，再用真实项目验证。

### 方向 B：先补输入或上下文

- 价值：可以选择一个真实新项目测试是否会正确建议 README、AGENTS、docs 和 Cursor rules。
- 风险：真实项目差异较大，可能需要额外适配。
- 建议：后续作为 real-case 项目验证。

### 方向 C：暂停并沉淀

- 价值：当前 workflow、template、scorecard 已完成沉淀。
- 风险：还未验证真实新项目。
- 建议：可以暂停，但建议继续建设已有项目接手工作流。

## 推荐下一步

推荐下一步：

```text
建设 project-understanding-workflow，用于已有项目接手时帮助 AI 读取上下文、理解结构和发现风险。
```

建议项目路径：

```text
12-projects/developer/capability-building/project-understanding-workflow/
```

## 待确认问题

- 是否先建设已有项目接手工作流。
- 是否需要同步开始设计 developer-kit 导出包结构。
- 是否需要找一个真实项目做新项目启动治理验证。
