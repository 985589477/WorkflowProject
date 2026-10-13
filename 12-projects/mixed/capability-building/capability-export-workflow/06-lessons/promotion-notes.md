# 沉淀记录

## 沉淀结论

能力导出工作流可以沉淀为 WorkflowProject 的通用能力。

## 已沉淀文件

```text
14-exports/README.md
05-standards/exported-kit-start-here-standard.md
04-workflows/common/capability-export-workflow.md
06-templates/common/capability-export-template.md
11-evaluations/output-scorecards/capability-export-scorecard.md
```

## 沉淀原因

- 当前项目已经能生产和沉淀能力，但缺少将能力拆分给外部角色独立使用的机制。
- 能力导出可以服务产品、开发、UI、测试等角色能力包。
- 导出能力需要保留来源、边界和使用方式，否则后续难以维护。

## 推荐下一步

使用该工作流导出第一个能力包：

```text
14-exports/product-manager-kit/
```

## 本轮导出沉淀

已完成第一个真实能力包：

```text
14-exports/product-manager-kit/
```

## 本轮经验

- 角色能力包不能只导出角色目录下的 workflow，还必须带上模板、评分表、角色定义和能力体系。
- 总入口文件非常关键，外部使用者不应该先理解所有细分工作流。
- 导出包需要一个 `START-HERE.md`，提供新项目或新 AI 对话中可直接复制的一句话启动。
- 导出包不需要复杂版本号，使用“导出时间”即可满足当前管理需求。
- 真实项目过程材料不应直接导出，应整理成示例后再放入 `examples/`。
- `manifest.md` 是能力包后续维护的关键文件，必须记录来源和未导出范围。

## 后续建议

下一步使用 `product-manager-kit` 跑一个真实或模拟任务，验证：

- 是否能独立启动。
- 是否能正确选择工作流。
- 是否缺少必要支撑文件。
- 是否需要补充示例。

## 导出包标准更新

后续所有能力包建议包含：

```text
START-HERE.md
README.md
usage-guide.md
manifest.md
```

其中：

- `START-HERE.md` 是统一能力包入口，不只放一句话启动。
- `manifest.md` 记录来源和导出时间。
- 不使用版本号，后续以导出时间判断新旧。

## START-HERE 统一格式

后续所有导出包的 `START-HERE.md` 必须包含：

```text
导出对象
导出时间
这个包能做什么
什么时候使用这个包
一句话启动
更短版本
外部自动读取配置
执行顺序
输出确认格式
使用原则
```

这样可以同时满足两类使用方式：

- 用户手动说“请使用某某能力包处理我的任务”。
- 新项目通过 `AI-WORKFLOW-RULES.md` 自动判断是否调用某个能力包。

## Skill 沉淀记录

产品经理能力包已进一步沉淀为 Codex skill：

```text
/Users/alpha/.codex/skills/product-manager-kit/
```

沉淀策略：

- `SKILL.md` 只保留触发边界、读取顺序、常见路由和输出要求。
- 完整能力包放入 `references/product-manager-kit/`。
- 使用时先读 `START-HERE.md`、`README.md`、`usage-guide.md` 和产品经理总入口工作流，再按任务读取具体 workflow、template 和 scorecard。

后续如果 `14-exports/product-manager-kit/` 更新，应同步更新该 skill 的 `references/product-manager-kit/`。

## 外部项目输出目录经验

外部项目使用导出包时，不能继续沿用 WorkflowProject 内部目录规则。

后续所有导出包和 skill 都应遵守：

- 用户明确指定输出目录时，使用用户指定目录。
- 目标项目已有统一文档目录时，优先使用已有目录。
- 常见可识别目录包括 `docs/`、`documents/`、`产品文档/`、`需求文档/`、`docs/product/`、`docs/prd/`、`product-docs/`。
- 目标项目没有合适目录时，才在项目根目录创建 `docs/`。
- 不要在外部项目中默认创建 `04-outputs/` 或 `12-projects/`。
