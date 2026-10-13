# 项目标准

## 项目目录必须包含

默认项目路径：

```text
12-projects/{角色}/{项目类型}/{项目名}/
```

项目类型：

```text
capability-building   能力建设项目
real-cases            真实使用项目
experiments           实验探索项目
```

项目内部结构必须包含：

```text
project-name/
├── README.md
├── 00-progress/
├── 01-inputs/
├── 02-analysis/
├── 03-prompts/
├── 04-outputs/
├── 05-review/
└── 06-lessons/
```

## 项目 README 必须说明

- 项目目标。
- 适用角色。
- 项目类型。
- 项目职责。
- 何时使用。
- 关键产物。
- 输入来源。
- 使用的工作流。
- 使用的模板。
- 当前状态。
- 当前进度记录位置。
- 重要决策记录位置。
- 下一步判断位置。
- 是否有内容提升到全局资产。

## 项目结束时

需要判断：

- 是否产生可复用模板。
- 是否产生可沉淀案例。
- 是否产生知识库条目。
- 是否需要归档。
- 是否完整记录关键阶段的调度角色和进度。
- 是否记录重要决策和下一步方向。

## 能力导出项目

如果项目目标是把某个角色或专项能力导出为独立能力包，应使用：

```text
04-workflows/common/capability-export-workflow.md
```

导出结果默认放入：

```text
14-exports/{能力包名称}/
```

导出包至少应包含：

```text
README.md
usage-guide.md
manifest.md
workflows/
templates/
scorecards/
```

如果包含案例，应放入：

```text
examples/
```

能力导出不是归档，也不是项目记录。导出包必须能脱离 WorkflowProject 独立使用。
