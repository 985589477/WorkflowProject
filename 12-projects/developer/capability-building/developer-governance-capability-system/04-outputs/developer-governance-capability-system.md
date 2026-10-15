# developer-kit 开发治理能力体系

## 定位

developer-kit 是一套 AI 协作开发治理体系。

它的目标不是教 Codex 或 Cursor “怎么写代码”，而是让 AI 在参与项目开发时能：

- 先理解项目，再修改项目。
- 先判断影响范围，再进入实现。
- 维护模块边界，而不是哪里方便改哪里。
- 控制风险等级，而不是所有任务都用同一套流程。
- 同步文档和验证结果，而不是只输出代码。
- 在新项目启动和已有项目接手时，主动补齐必要开发规范。

一句话：

```text
developer-kit 是 Codex / Cursor 的开发治理护栏，不是限制模型能力的铁轨。
```

## 适用场景

- 新项目启动，需要建立 AI 协作开发规范。
- 已有项目接手，需要让 AI 快速理解项目结构。
- 产品需求进入开发，需要判断模块影响范围。
- 多模块协作，需要明确模块边界和交互方式。
- 准备新增模块，需要判断是否真的应该新增。
- 开发任务涉及代码修改、测试、文档同步和交付说明。
- 项目长期维护，需要控制技术债、风险和发布质量。

## 不适用场景

- 用户只想问一个非常简单的技术概念。
- 用户明确要求只做一次轻量修改，且风险极低。
- 项目已有更明确、更具体的本地开发规则。
- 任务属于产品、设计、测试、运营等非开发治理范畴。

遇到这些情况时，应轻量使用 developer-kit，不能强行套完整流程。

## 与 Codex / Cursor 的协作关系

| 对象 | 主要职责 |
| --- | --- |
| Codex | 读代码、改代码、跑测试、执行命令、总结变更 |
| Cursor | 编辑器内上下文协作、局部代码修改、规则文件辅助 |
| developer-kit | 定义项目治理、模块边界、风险分级、交付和文档同步规则 |

developer-kit 应该能导出为：

```text
Codex skill
Cursor rules
AGENTS.md
项目 docs/development-standard.md
```

## 核心原则

### 1. 护栏优先

developer-kit 不应限制 AI 的工程判断，而应提供安全边界。

### 2. 本地规则优先

项目已有的 `README.md`、`AGENTS.md`、`.cursor/rules/`、测试脚本和架构文档优先级高于通用 developer-kit。

### 3. 按风险分级执行

小任务轻量执行，中高风险任务必须先分析。

### 4. 模块边界优先

代码修改必须优先考虑模块职责和协作边界。

### 5. 交付闭环

开发完成不等于任务完成，必须考虑验证、文档、风险和后续建议。

## 能力地图

| 编号 | 能力 | 解决的问题 |
| --- | --- | --- |
| 01 | 需求入口治理 | 防止需求不清就直接开发 |
| 02 | 项目结构治理 | 让新项目和已有项目有清晰结构 |
| 03 | 模块边界治理 | 明确模块负责什么、不负责什么 |
| 04 | 模块协作设计 | 明确模块之间如何调用、传参和依赖 |
| 05 | 新增模块判断 | 防止乱拆模块或模块过度膨胀 |
| 06 | 架构决策记录 | 记录为什么这样设计 |
| 07 | 影响范围分析 | 判断改动影响哪些模块、页面、接口和数据 |
| 08 | 变更风险分级 | 根据风险决定是否需要方案和人工确认 |
| 09 | 数据与状态治理 | 管理数据模型、状态归属和状态修改权限 |
| 10 | 实现执行工作流 | 稳定完成代码修改 |
| 11 | 测试与验收 | 明确如何验证完成 |
| 12 | 文档同步 | 保证代码、架构、接口和说明同步更新 |
| 13 | 代码评审 | 检查 bug、风险、边界和可维护性 |
| 14 | 交付说明 | 输出变更说明、验证结果和风险 |
| 15 | AI 协作复盘 | 发现 AI 协作失控点并反哺规则 |
| 16 | 权限与危险操作治理 | 防止 AI 自动执行高风险操作 |
| 17 | 环境与配置治理 | 管理 env、依赖、启动、构建和部署配置 |
| 18 | 依赖与技术债治理 | 控制新增依赖、临时方案和重构范围 |
| 19 | 观测与问题追踪治理 | 管理日志、错误、问题复现和线上故障 |
| 20 | 版本与发布治理 | 管理发布检查、回滚和上线后观察 |

## 新项目启动检查

新项目开始时，AI 应检查是否存在：

```text
README.md
AGENTS.md 或 AI 协作规则
docs/
docs/architecture/
docs/development-standard.md
docs/quality-checklist.md
package.json / pyproject.toml / Cargo.toml 等技术栈入口
测试命令
构建命令
环境变量说明
模块目录说明
```

如果缺失，应建议补充，而不是直接开始堆代码。

## 已有项目接手检查

AI 接手已有项目时，建议先阅读：

```text
README.md
AGENTS.md
.cursor/rules/
package.json 或等价技术栈入口
docs/architecture/
docs/development-standard.md
主要源码目录
测试目录
最近变更记录
```

然后输出：

```text
项目技术栈
启动方式
测试方式
主要模块
缺失文档
潜在风险
建议补齐内容
```

## 产品需求进入开发后的处理流程

收到产品需求后，不直接写代码。先判断：

- 需求是否清楚。
- 成功标准是否明确。
- 是否有不做范围。
- 是否属于已有模块。
- 是否需要新增模块。
- 是否涉及跨模块协作。
- 是否涉及数据结构变化。
- 是否涉及权限、支付、登录、配置、迁移等高风险区域。
- 是否需要产品确认。

推荐产物：

```text
需求开发简报
影响范围分析
模块变更建议
风险等级
待确认问题
```

## 模块边界标准

每个核心模块应能说明：

```text
模块职责
不负责范围
对外能力
输入
输出
依赖模块
被调用方
关键数据结构
边界规则
常见变更点
风险
```

模块边界不清时，不应直接进入实现，应先补模块契约。

## 模块协作标准

模块协作要说明：

- 谁调用谁。
- 传入什么。
- 返回什么。
- 异常如何处理。
- 状态由谁拥有。
- 数据由谁持久化。
- 哪些依赖不允许反向调用。

推荐维护：

```text
docs/architecture/module-map.md
docs/architecture/module-interactions.md
docs/architecture/module-contracts/
```

## 新增模块判断标准

适合新增模块的情况：

- 出现新的稳定业务概念。
- 已有模块职责明显过载。
- 新能力有独立生命周期。
- 新能力会被多个地方复用。
- 新能力有独立数据模型。
- 新能力需要独立测试。

不适合新增模块的情况：

- 只是一个小工具函数。
- 只是一个页面局部逻辑。
- 只是临时需求。
- 只是为了让文件看起来更整齐。
- 没有独立业务含义。

## 模块开发结构建议

前端模块可参考：

```text
module-name/
├── README.md
├── index.ts
├── types.ts
├── api.ts
├── service.ts
├── components/
├── hooks/
├── utils/
└── tests/
```

后端模块可参考：

```text
module-name/
├── README.md
├── routes/
├── service/
├── model/
├── repository/
├── dto/
├── tests/
└── module-contract.md
```

具体结构应优先遵循项目已有技术栈和目录风格。

## 变更风险分级

| 等级 | 类型 | 执行方式 |
| --- | --- | --- |
| 低风险 | 文案、样式、小 bug、单文件小改 | 可直接执行，简短说明 |
| 中风险 | 单模块功能、局部接口、局部状态 | 先做影响分析，再执行 |
| 高风险 | 跨模块、数据结构、权限、登录、支付、核心流程 | 先给方案，等待确认 |
| 危险变更 | 删除数据、迁移、批量重构、生产配置、破坏性命令 | 必须人工确认，必要时拒绝自动执行 |

## 必须人工确认的情况

- 删除或迁移数据。
- 修改生产配置。
- 修改登录、权限、支付、计费。
- 大范围重构。
- 批量重命名或移动文件。
- 引入大型新依赖。
- 修改核心架构。
- 测试无法运行但改动风险较高。
- 需求不清但会影响多个模块。

## 后续工作流建设顺序

第一阶段：先管住项目不失控。

```text
1. project-bootstrap-workflow
2. project-understanding-workflow
3. requirement-to-architecture-workflow
4. module-boundary-analysis-workflow
5. change-risk-assessment-workflow
6. impact-analysis-workflow
```

第二阶段：管住开发过程。

```text
7. implementation-workflow
8. testing-verification-workflow
9. documentation-sync-workflow
10. code-review-workflow
```

第三阶段：管住长期维护。

```text
11. architecture-decision-record-workflow
12. dependency-and-tech-debt-workflow
13. environment-config-governance-workflow
14. release-and-rollback-workflow
15. ai-collaboration-retrospective-workflow
```

## 导出形态建议

developer-kit 后续应支持：

```text
14-exports/developer-kit/
~/.codex/skills/developer-kit/
.cursor/rules/developer-kit.mdc
AGENTS.md
docs/development-standard.md
```

## 风险与待确认问题

- 不同技术栈的模块结构可能差异很大，后续需要按前端、后端、全栈、移动端继续细化。
- Cursor 规则、Codex skill、AGENTS.md 的格式不同，后续需要做适配器。
- 需要用真实项目验证 developer-kit 是否会过度流程化。
- 需要明确哪些规范属于“建议”，哪些属于“必须遵守”。
