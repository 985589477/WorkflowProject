# 快速开始

这份文档只回答一个问题：我现在有一个想法或一份材料，下一步该做什么？

## 最短路径

如果你只是想完成一次任务，按这 6 步走：

```text
1. 创建项目
2. 把想法整理成标准输入
3. 分析输入
4. 生成正式提示词
5. 执行 AI 并保存输出
6. 评审并决定是否沉淀

## 如果你要让 AI 开发真实代码项目

不要先从具体角色开始。先使用项目治理主流程：

```text
请先使用 project-governance-workflow 检查当前项目的规则、架构、模块、设计规范、任务列表和模块文档。
如果缺少关键材料，请先列出缺口并和我确认；如果材料已经存在，请按项目文档规划并执行开发。
不要在治理检查完成前直接大范围修改代码。
```

对应文件：

```text
04-workflows/common/project-governance-workflow.md
06-templates/common/project-governance-checklist-template.md
05-standards/project-governance-standard.md
```

只有当治理流程判断确实需要专业能力时，才继续调用产品、UI、开发或测试角色。
```

## 如果只是想使用现成角色能力包

如果你不是要创建 WorkflowProject 内部项目，而是想在其他项目里直接使用已经导出的角色能力包，优先看：

```text
14-exports/product-manager-kit/START-HERE.md
14-exports/developer-kit/START-HERE.md
14-exports/ui-designer-kit/START-HERE.md
14-exports/tester-kit/START-HERE.md
```

产品经理任务：

```text
请使用 product-manager-kit 处理我的产品任务：{写下你的任务}
```

开发任务：

```text
请使用 developer-kit 协助我处理这个开发任务：{写下你的任务}
```

UI 设计任务：

```text
请使用 ui-designer-kit 处理我的设计任务：{写下你的任务}
```

测试任务：

```text
请使用 tester-kit 处理我的测试任务：{写下你的任务}
```

如果是第一次把能力包复制到外部项目，先看：

```text
14-exports/{kit-name}/INSTALL.md
```

如果要建设新的角色能力包，必须参考：

```text
05-standards/role-kit-lifecycle-standard.md
```

如果你不知道当前项目里有哪些能力可以直接用，先看：

```text
12-projects/asset-index.md
```

它按角色能力包、工作流、模板、评分表、标准和工具脚本整理可用资产。

## 第 1 步：创建项目

优先使用脚本创建项目：

```bash
python3 tools/create_project.py mixed my-first-task --type real-cases
```

常见角色：

```text
mixed              跨角色任务
product-manager    产品经理任务
developer          开发任务
ui-designer        UI 设计任务
tester             测试任务
```

如果不知道该选哪个角色：

```text
写 PRD、需求分析、功能规划 -> product-manager
代码实现、bug 修复、技术方案 -> developer
页面设计、交互说明、组件说明 -> ui-designer
测试计划、测试用例、回归范围 -> tester
框架搭建、流程设计、多角色任务 -> mixed
不确定归哪类 -> mixed
```

创建后会得到：

```text
12-projects/{角色}/{项目类型}/{项目名}/
├── README.md
├── 00-progress/
├── 01-inputs/
├── 02-analysis/
├── 03-prompts/
├── 04-outputs/
├── 05-review/
└── 06-lessons/
```

执行过程中，关键进度会记录到：

```text
12-projects/{角色}/{项目类型}/{项目名}/00-progress/progress-log.md
```

持续迭代项目的当前状态摘要会记录到：

```text
12-projects/{角色}/{项目类型}/{项目名}/00-progress/memory-summary.md
```

后续继续项目时，优先读 `memory-summary.md`，不要每次都读完整历史。

常见项目类型：

```text
capability-building   建设角色能力、工作流、模板和评分表
real-cases            使用已有能力处理真实业务任务
experiments           探索不稳定想法
```

如果是混合角色项目，并且你想指定项目根目录，可以使用：

```bash
python3 tools/create_project.py mixed ai-template-tool --output 12-projects/mixed/real-cases/ai-template-tool
```

`--output` 只决定项目根目录，项目内部仍然自动生成标准结构。

## 第 2 步：把想法整理成标准输入

如果你只有一句想法，例如：

```text
我想做一个产品经理 workflow。
```

先使用：

```text
06-templates/meta/idea-to-input-generator.md
```

配合这个工作流：

```text
04-workflows/common/idea-to-input-workflow.md
```

生成一份标准输入文档，并保存到：

```text
12-projects/{角色}/{项目类型}/{项目名}/01-inputs/original-requirement.md
```

如果你已经有完整材料，把你的原始资料直接放入：

```text
12-projects/{角色}/{项目类型}/{项目名}/01-inputs/
```

可以放：

- 想法草稿
- 需求说明
- 会议纪要
- 参考资料
- 截图说明
- 代码问题

## 什么是标准输入

标准输入不是随便放一段话，而是要让 AI 明确知道：

```text
用户原始描述
背景
目标
原始材料
约束条件
AI 推断
待确认信息
推荐后续流程
```

如果你不想自己整理，就直接让 AI 使用：

```text
06-templates/meta/idea-to-input-generator.md
```

## 执行中如何汇报进度

后续执行项目时，每个关键节点都建议在对话中输出：

```text
当前进度：
调度角色：
使用工作流：
使用模板：
下一步：
```

同时把关键节点写入：

```text
00-progress/progress-log.md
```

如果项目会持续迭代，还要在阶段结束时更新：

```text
00-progress/memory-summary.md
```

这样下一次继续项目时，AI 可以先读当前摘要，再按需追溯历史。

对应规则见：

```text
00-system/progress-reporting-rules.md
```

如果你看不懂 AI 做了什么，要求 AI 使用：

```text
06-templates/meta/explainable-project-runner.md
```

它会在执行前说明、执行后解释，并帮助你维护：

```text
00-progress/decision-log.md
00-progress/next-actions.md
```

## 第 3 步：分析输入

使用这个工作流：

```text
04-workflows/common/input-analysis-workflow.md
```

把分析结果保存到：

```text
12-projects/{角色}/{项目类型}/{项目名}/02-analysis/input-analysis.md
```

## 第 4 步：生成正式提示词

如果已经有模板，用：

```text
06-templates/meta/prompt-generator.md
```

如果还没有模板，先用：

```text
06-templates/meta/template-generator.md
```

正式提示词保存到：

```text
12-projects/{角色}/{项目类型}/{项目名}/03-prompts/final-prompt.md
```

## 第 5 步：执行 AI 并保存输出

把正式提示词交给 AI 执行。

把输出保存到：

```text
12-projects/{角色}/{项目类型}/{项目名}/04-outputs/
```

## 第 6 步：评审并决定是否沉淀

使用：

```text
06-templates/meta/output-reviewer.md
```

评审结果保存到：

```text
12-projects/{角色}/{项目类型}/{项目名}/05-review/output-review.md
```

如果结果很好，再使用：

```text
04-workflows/common/asset-promotion-workflow.md
```

判断它应该提升为：

- 模板
- 优秀案例
- 知识库内容
- 评估方法
- 或仅归档

## 我迷路时看哪里

- 不知道项目怎么开：看本文档。
- 不知道目录放什么：看 `13-visual-maps/WorkflowProject-file-responsibility-outline.md`。
- 不知道整体流程：看 `13-visual-maps/WorkflowProject-operation-flow-outline.md`。
- 不知道当前有什么、能用什么、风险在哪：看 `15-dashboard/`。
- 不知道术语含义：看 `00-system/terminology.md`。
- 不知道是否合格：看 `05-standards/`。
- 不知道 AI 做了什么：看 `00-system/result-report-rules.md`。
- 不知道为什么这么做：看项目里的 `00-progress/decision-log.md`。
- 不知道下一步怎么选：看项目里的 `00-progress/next-actions.md`。
