# 版本规则

## 版本使用场景

需要版本号的内容：

- 通用模板
- 角色模板
- 标准文档
- 关键工作流
- 评分表和评估 rubrics

通常不需要版本号的内容：

- 一次性输入资料
- 单次输出结果
- 临时草稿

## 文件版本

当一个模板或标准发生明显行为变化时，使用文件名版本：

```text
prd-generation-template.v1.md
prd-generation-template.v2.md
```

小修小补可以直接更新当前文件，并在文件中记录变更说明。

## 推荐文档头部

```md
# 文档标题

状态: draft | active | reviewed | deprecated
版本: v1
负责人: 角色或人员
更新日期: YYYY-MM-DD
```
