# WorkflowProject

WorkflowProject 是一个面向 AI 协作的工作流文档工程框架。

它的目标不是简单收集提示词，而是管理一条完整的生产链路：

```text
input 原始资料
-> workflow AI 协作流程
-> template 可复用模板
-> prompt 正式提示词
-> output AI 输出结果
-> review 质量评审
-> example 优秀案例
-> knowledge 可复用知识
-> export 独立能力包
```

## 核心原则

- 所有内容都要有明确归属：系统规则、治理规则、角色、输入、工作流、模板、正式提示词、输出、案例或知识。
- 模板不等于正式提示词。模板是可复用骨架，正式提示词是填入具体输入后的执行版本。
- 案例不等于普通输出。只有经过评审、具备复用价值的任务结果才能进入案例库。
- 任何重要结构调整都需要留下决策记录，避免后续反复推翻。
- AI 可以参与生成、评审和优化，但项目本身必须用标准和治理规则约束 AI 的产物。
- 文档正文默认使用中文，除路径、命令、状态值和必要技术术语外，不使用不必要的英文。

## 我现在该怎么用

如果你是第一次使用，不要从所有目录开始看，先看：

```text
00-system/quick-start.md
```

如果要创建一个新项目，直接运行：

```bash
python3 tools/create_project.py mixed my-first-task --type real-cases
```

默认会创建到：

```text
12-projects/{角色}/{项目类型}/{项目名}/
```

如果要刷新全部导图，运行：

```bash
python3 tools/refresh_maps.py
```

如果想用可视化界面理解当前项目状态，运行：

```bash
cd 15-dashboard
npm install
npm run dev
```

可视化控制台的数据由 `tools/generate_dashboard_data.py` 生成。运行 `python3 tools/refresh_maps.py` 时，会同步刷新控制台数据和 XMind 导图。

如果项目变多，先看项目索引：

```text
12-projects/project-index.md
```

然后只需要先关注新项目里的这几个目录：

```text
00-progress/  放执行进度和调度记录
01-inputs/    放原始材料
02-analysis/  放材料分析
03-prompts/   放正式提示词
04-outputs/   放 AI 输出
05-review/    放质量评审
06-lessons/   放复盘和沉淀建议
```

全局目录先不用全部理解。需要时再查对应标准、模板或工作流。

执行项目时，对话中会优先说明：

```text
当前进度
调度角色
使用工作流
使用模板
下一步
```

如果你希望 AI 每一步都解释“做了什么、为什么做、你该看哪里”，使用：

```text
06-templates/meta/explainable-project-runner.md
```

## 目录结构

```text
00-system/          项目系统设计、架构、术语、生命周期和操作指南
01-governance/      项目维护规则、变更规则、评审流程和质量门禁
02-roles/           AI 协作角色定义，如产品经理、程序员、UI 设计师
03-inputs/          原始资料和参考材料
04-workflows/       从输入到模板、提示词、输出、案例的 AI 协作流程
05-standards/       输入、模板、提示词、输出、案例和评审标准
06-templates/       可复用提示词模板，包括 meta 模板和角色模板
07-prompts/         已填充输入、准备交给 AI 执行的正式提示词
08-outputs/         AI 基于正式提示词生成的输出结果
09-examples/        经评审后值得长期参考的优秀案例包
10-knowledge-base/  从案例中提炼出的模式、反模式、最佳实践和复用片段
11-evaluations/     提示词和输出的测试、评分、对比与评估标准
12-projects/        具体任务项目，每个项目可拥有自己的输入、提示词、输出和复盘
13-visual-maps/     XMind 导图和对应 Markdown 大纲
14-exports/         从项目中导出的独立角色能力包或专项能力包
15-dashboard/       React 可视化控制台
99-archive/         过时、废弃或历史保留内容
```

## 标准工作方式

1. 在 `12-projects/` 下创建具体任务项目。
2. 将原始资料放入项目内输入目录，或全局 `03-inputs/`。
3. 选择 `04-workflows/` 中的工作流。
4. 使用 `06-templates/meta/` 让 AI 辅助生成或优化角色模板。
5. 使用角色模板生成正式提示词，并放入 `07-prompts/` 或项目内 prompts 目录。
6. 执行 AI 后，将结果放入 `08-outputs/` 或项目内 outputs 目录。
7. 根据 `05-standards/` 和 `11-evaluations/` 完成评审。
8. 将优秀任务沉淀为 `09-examples/` 案例包。
9. 将可复用规律提炼到 `10-knowledge-base/`。
10. 如果某个角色能力需要脱离当前项目使用，将能力导出到 `14-exports/`。
11. 将过时内容移动到 `99-archive/`。

## 优先阅读

- `00-system/quick-start.md`
- `00-system/progress-reporting-rules.md`
- `00-system/execution-brief-rules.md`
- `00-system/result-report-rules.md`
- `06-templates/meta/project-runner.md`
- `06-templates/meta/explainable-project-runner.md`
- `10-knowledge-base/patterns/framework-bootstrap-pattern.md`
- `00-system/architecture.md`
- `00-system/operating-guide.md`
- `00-system/document-lifecycle.md`
- `00-system/language-rules.md`
- `02-roles/role-registry.md`
- `01-governance/change-management.md`
- `01-governance/quality-gates.md`
- `05-standards/role-standard.md`
- `05-standards/workflow-standard.md`
- `05-standards/template-standard.md`
- `05-standards/prompt-standard.md`
- `05-standards/project-standard.md`
- `12-projects/project-template/README.md`

## 新增内容前检查

新增任何文档前，先判断它属于哪一类：

```text
规则 -> 00-system 或 01-governance
角色能力 -> 02-roles
原始资料 -> 03-inputs
处理方法 -> 04-workflows
质量约束 -> 05-standards
可复用骨架 -> 06-templates
本次执行提示词 -> 07-prompts
AI 结果 -> 08-outputs
优秀案例 -> 09-examples
经验规律 -> 10-knowledge-base
评估记录 -> 11-evaluations
具体任务集合 -> 12-projects
可视化导图 -> 13-visual-maps
外部能力包 -> 14-exports
可视化控制台 -> 15-dashboard
历史保留 -> 99-archive
```
