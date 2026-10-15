# 工作流标准

## 工作流必须包含

- 目的。
- 适用场景。
- 输入要求。
- 执行步骤。
- 输出结果。
- 质量检查。

## 推荐结构

```md
# 工作流名称

## 目的

## 适用场景

## 输入要求

## 执行步骤

## 输出结果

## 质量检查
```

## 注意事项

- Workflow 描述方法，不直接替代 prompt。
- Workflow 可以引用 template、standard 和 evaluation。
- 角色工作流应优先复用 common workflow，再补充角色特有步骤。

## 角色总入口工作流补充要求

如果某个 workflow 是角色能力包的总入口，例如：

```text
product-manager-workflow.md
developer-kit-workflow.md
```

它不能只做单点任务分流，必须符合：

```text
05-standards/role-kit-lifecycle-standard.md
```

至少包含：

- 角色生命周期。
- 阶段推进规则。
- 关键阶段门禁。
- 主动询问规则。
- 执行状态格式。
- 任务结束标准。
- 后续流转判断。
