# 产品经理能力体系

## 体系目标

产品经理能力体系用于指导后续产品经理角色的持续建设。

它不是单个文档，也不是一次性补全所有模板，而是一张产品经理能力地图，用来回答：

```text
产品经理可以做哪些类型的任务？
每类任务需要什么输入？
会产出什么结果？
需要哪些 workflow、template、example 和 evaluation 支撑？
哪些能力应该先建设？
后续应该创建哪些项目来验证？
```

## 设计原则

### 先总控，后细分

先保留 `product-manager-workflow.md` 作为产品经理总入口，再按真实任务逐步拆出细分能力。

### 先项目验证，再沉淀资产

每个能力模块不应直接写成全局模板。应先创建 `12-projects/product-manager/` 下的真实项目，跑通后再沉淀。

### 能力不是文件名

能力模块要对应真实工作能力，例如“需求分析”“PRD 生成”“用户反馈洞察”，而不是只对应某个 Markdown 文件。

### 每个能力都要有闭环

每个能力模块至少要能回答：

- 输入是什么。
- 处理过程是什么。
- 输出是什么。
- 如何评审。
- 何时沉淀。

### 控制扩展节奏

不一次性补齐所有能力。优先建设最常用、最能验证框架价值的能力。

## 能力分层

产品经理能力体系分为四层。

### 第 1 层：入口能力

解决“用户只有想法，如何启动项目”的问题。

核心能力：

- 想法转输入。
- 任务类型判断。
- 产品目标和边界确认。

已有支撑：

```text
06-templates/meta/idea-to-input-generator.md
04-workflows/product-manager/product-manager-workflow.md
```

### 第 2 层：核心产出能力

解决“产品经理最常见要产出什么”的问题。

核心能力：

- 需求分析。
- PRD 生成。
- 功能规划。
- 用户故事生成。
- 验收标准生成。

### 第 3 层：判断和决策能力

解决“产品经理如何做取舍”的问题。

核心能力：

- 功能优先级判断。
- 版本规划。
- 产品策略判断。
- 风险和边界识别。

### 第 4 层：外部输入处理能力

解决“从外部材料中提炼产品机会”的问题。

核心能力：

- 用户反馈整理。
- 竞品分析。
- 数据现象分析。
- 会议纪要转需求。

## 能力模块总览

| 能力模块 | 主要职责 | 典型输入 | 典型输出 | 优先级 |
| --- | --- | --- | --- | --- |
| 想法转输入 | 把模糊想法变成标准 input | 一句话想法、零散描述 | `original-requirement.md` | 已具备 |
| 需求分析 | 明确问题、用户、场景、目标和约束 | 需求草稿、业务背景 | 需求分析文档 | 高 |
| PRD 生成 | 生成可评审的产品需求文档 | 标准 input、需求分析 | PRD | 高 |
| 功能规划 | 拆分功能范围和模块 | 产品目标、业务约束 | 功能清单、范围说明 | 高 |
| 用户故事 | 把需求转成用户视角表达 | 需求分析、用户场景 | 用户故事 | 中 |
| 验收标准 | 明确功能完成标准 | PRD、功能清单 | 验收标准 | 高 |
| 用户反馈整理 | 从反馈中提炼问题和机会 | 用户反馈、客服记录 | 问题归类、机会列表 | 中 |
| 竞品分析 | 从竞品中提炼差异和启发 | 竞品资料、截图 | 竞品分析报告 | 中 |
| 优先级判断 | 判断先做什么后做什么 | 功能列表、目标、成本 | 优先级建议 | 中 |
| 版本规划 | 规划阶段目标和发布节奏 | 优先级、资源、目标 | 版本路线图 | 中 |
| 产品策略判断 | 判断方向是否值得做 | 市场、用户、目标 | 策略建议 | 低 |

## 核心能力模块

### 需求分析

职责：

把用户想法、业务目标或原始材料整理成清晰需求。

典型任务：

- 分析用户真正要解决的问题。
- 提取目标用户和使用场景。
- 标记事实、推断和待确认信息。
- 明确需求边界。

需要建设：

- `04-workflows/product-manager/requirement-analysis-workflow.md`
- `06-templates/product-manager/requirement-analysis-template.md`
- `11-evaluations/output-scorecards/requirement-analysis-scorecard.md`

推荐项目：

```bash
python3 tools/create_project.py product-manager requirement-analysis-workflow --type capability-building
```

### PRD 生成

职责：

把标准输入和需求分析转成可评审的 PRD。

典型任务：

- 生成背景、目标、用户场景、功能范围。
- 输出功能说明和规则。
- 保留待确认问题。
- 为设计和开发提供下游输入。

需要建设：

- `04-workflows/product-manager/prd-workflow.md`
- `06-templates/product-manager/prd-template.md`
- `11-evaluations/output-scorecards/prd-scorecard.md`

推荐项目：

```bash
python3 tools/create_project.py product-manager prd-workflow --type capability-building
```

### 功能规划

职责：

把产品目标拆成可执行功能范围。

典型任务：

- 拆分功能模块。
- 区分必须做、可选做、暂不做。
- 明确版本范围。
- 输出功能清单。

需要建设：

- `04-workflows/product-manager/feature-planning-workflow.md`
- `06-templates/product-manager/feature-planning-template.md`

推荐项目：

```bash
python3 tools/create_project.py product-manager feature-planning-workflow --type capability-building
```

### 验收标准

职责：

把产品需求转成可验证的完成标准。

典型任务：

- 输出功能验收条件。
- 明确异常状态。
- 明确边界情况。
- 帮助开发和测试理解完成标准。

需要建设：

- `04-workflows/product-manager/acceptance-criteria-workflow.md`
- `06-templates/product-manager/acceptance-criteria-template.md`

推荐项目：

```bash
python3 tools/create_project.py product-manager acceptance-criteria-workflow --type capability-building
```

### 用户反馈整理

职责：

从零散反馈中提炼用户问题、需求机会和优先级线索。

典型任务：

- 反馈归类。
- 提取痛点。
- 标记高频问题。
- 形成需求机会池。

需要建设：

- `04-workflows/product-manager/user-feedback-workflow.md`
- `06-templates/product-manager/user-feedback-template.md`

推荐项目：

```bash
python3 tools/create_project.py product-manager user-feedback-workflow --type capability-building
```

### 竞品分析

职责：

从竞品资料中提炼可参考的产品结构、交互策略和差异机会。

典型任务：

- 竞品功能拆解。
- 差异点分析。
- 可借鉴点提炼。
- 风险和误区识别。

需要建设：

- `04-workflows/product-manager/competitor-analysis-workflow.md`
- `06-templates/product-manager/competitor-analysis-template.md`

推荐项目：

```bash
python3 tools/create_project.py product-manager competitor-analysis-workflow --type capability-building
```

## 建设优先级

### 第一阶段：把产品经理最小闭环跑通

优先建设：

1. 需求分析。
2. PRD 生成。
3. 验收标准。

原因：

这三项能形成最常见的产品交付链路：

```text
想法
-> 标准 input
-> 需求分析
-> PRD
-> 验收标准
```

### 第二阶段：增强规划和判断

继续建设：

1. 功能规划。
2. 优先级判断。
3. 版本规划。

原因：

这些能力用于处理多个功能、多阶段建设和资源取舍。

### 第三阶段：处理外部输入

继续建设：

1. 用户反馈整理。
2. 竞品分析。
3. 数据现象分析。
4. 会议纪要转需求。

原因：

这些能力依赖更多真实材料，适合在后续有具体输入时建设。

## 后续项目拆分

推荐下一批真实项目按顺序启动。

### 项目 1：需求分析工作流

目的：

生成并验证需求分析细分 workflow。

建议创建：

```bash
python3 tools/create_project.py product-manager requirement-analysis-workflow --type capability-building
```

沉淀目标：

```text
04-workflows/product-manager/requirement-analysis-workflow.md
```

### 项目 2：PRD 生成工作流

目的：

生成并验证 PRD 细分 workflow。

建议创建：

```bash
python3 tools/create_project.py product-manager prd-workflow --type capability-building
```

沉淀目标：

```text
04-workflows/product-manager/prd-workflow.md
06-templates/product-manager/prd-template.md
```

### 项目 3：验收标准工作流

目的：

生成并验证验收标准细分 workflow。

建议创建：

```bash
python3 tools/create_project.py product-manager acceptance-criteria-workflow --type capability-building
```

沉淀目标：

```text
04-workflows/product-manager/acceptance-criteria-workflow.md
```

## 沉淀路径

### 能力体系地图

沉淀到：

```text
10-knowledge-base/patterns/product-manager-capability-system.md
```

用途：

作为产品经理能力建设的总地图。

### 角色定义补充

可补充到：

```text
02-roles/product-manager/role-definition.md
```

用途：

让产品经理角色不只描述职责，还能看到能力结构。

### 工作流入口补充

可补充到：

```text
04-workflows/product-manager/README.md
```

用途：

让用户知道产品经理工作流目录未来会如何扩展。

### 细分工作流

后续逐步沉淀到：

```text
04-workflows/product-manager/
```

### 细分模板

后续逐步沉淀到：

```text
06-templates/product-manager/
```

### 评估标准

后续逐步沉淀到：

```text
11-evaluations/output-scorecards/
```

## 质量检查

检查产品经理能力体系是否合格：

- 是否从总工作流延伸，而不是另起一套规则。
- 是否按能力模块组织，而不是按文件名堆叠。
- 是否明确每个能力的输入和输出。
- 是否明确每个能力后续需要建设的资产。
- 是否有优先级。
- 是否能指导下一批项目创建。
- 是否避免一次性补完所有细分文档。

## 使用方式

当用户想继续建设产品经理能力时，先看本体系。

如果不知道下一步做什么，优先选择第一阶段项目：

```text
需求分析工作流
PRD 生成工作流
验收标准工作流
```

每个细分能力都应按项目链路执行：

```text
模糊想法
-> 标准 input
-> 输入分析
-> 正式提示词
-> 输出
-> 评审
-> 沉淀
```

不要直接在全局目录手写大量细分文件。先通过项目验证，再沉淀到全局资产。
