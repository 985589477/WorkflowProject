# 原始需求

## 用户目标

用户希望下载并查看 GitHub 上的 Ponytail 项目内容，然后把其中有价值的能力融合进当前 WorkflowProject 的 `developer-kit`。

用户进一步补充：

```text
也可以尝试原文搬进来融合进来成一个角色
```

## 需求理解

这不是要把 Ponytail 原封不动作为第三方工具运行，而是要吸收它的开发协作思想，转化成当前开发角色中的一个可调度能力。

核心诉求：

- 降低 AI 开发时过度设计、过度抽象、过度新增文件和依赖的概率。
- 让 developer-kit 在实现前主动判断“是否真的需要写代码”。
- 让 Codex、Cursor 等开发型 AI 在已有项目中优先复用项目能力。
- 在不牺牲安全、校验、错误处理、可访问性和测试的前提下，尽量少写代码。

## 外部参考

Ponytail 项目：

```text
https://github.com/DietrichGebert/ponytail
```

本次下载到临时目录：

```text
/tmp/ponytail
```

许可证：

```text
MIT License
```

## 需要融合的位置

- 开发角色定义。
- developer-kit 总入口。
- 实现工作流。
- 代码评审工作流。
- 模板。
- 评分表。
- 知识库。
- 导出包。
