# 使用的模板能力

## 使用的 Meta 模板

本项目验证了以下 meta 模板能力：

- `06-templates/meta/template-generator.md`
- `06-templates/meta/prompt-generator.md`
- `06-templates/meta/output-reviewer.md`
- `06-templates/meta/example-extractor.md`
- `06-templates/meta/template-optimizer.md`

## 使用的通用模板

- `06-templates/common/general-task-template.md`

## 模板使用方式

本项目不是直接套用单一角色模板，而是使用 meta 模板能力完成：

```text
原始需求
-> 抽象框架结构
-> 生成正式提示词
-> 评审输出
-> 提取案例
-> 反向优化项目规范
```

## 可复用结论

当任务是“搭建框架、设计流程、建立规范、跨角色协作”时，应优先使用：

```text
mixed 角色
通用工作流
meta 模板
项目执行总控工作流
进度汇报规则
```
