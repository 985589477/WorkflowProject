# 决策记录

## 使用说明

这里记录项目执行过程中重要决策的原因。

进度记录回答“做到了哪一步”，决策记录回答“为什么这么做”。

## 记录模板

```md
## 决策：{决策标题}

### 背景

为什么出现这个问题？

### 决策

最终决定做什么？

### 原因

为什么这样做？

### 影响

这个决策会影响哪些文件、流程或后续方向？

### 日期

YYYY-MM-DD
```

## 决策：用 framework-refresh 取代 bootstrap 作为当前框架说明

### 背景

`workflowproject-framework-bootstrap` 记录的是项目早期从 0 到 1 的搭建过程。当前项目已经新增可视化导图、React dashboard、能力导出层、执行 skill 和产品经理完整能力体系。

### 决策

创建 `workflowproject-framework-refresh`，作为当前框架的最新同步记录。

旧 bootstrap 保留历史价值，但不再作为当前框架说明。

### 原因

如果继续让 bootstrap 留在当前项目索引中，会让用户误以为它代表当前最新框架，实际它已经无法覆盖 `14-exports/`、`15-dashboard/` 和完整角色能力体系。

### 影响

- 当前框架说明以 refresh 项目为准。
- bootstrap 将归档到 `99-archive/projects/`。
- 项目索引会更清爽。

### 日期

2026-10-13
