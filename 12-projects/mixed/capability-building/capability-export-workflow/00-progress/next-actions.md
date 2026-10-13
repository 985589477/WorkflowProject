# 下一步判断

## 使用说明

这里用于帮助用户判断项目下一步该往哪里走。

## 当前项目状态

已完成第一版，并已完成第一次真实导出。

能力导出工作流、模板、评分表和 `14-exports/` 导出区已沉淀到全局目录。

已导出：

```text
14-exports/product-manager-kit/
```

已增强：

```text
14-exports/product-manager-kit/START-HERE.md
```

能力包现在使用导出时间管理，不使用版本号。

`START-HERE.md` 已升级为所有导出包的统一入口格式，后续导出任何角色或专项能力包时都应包含：

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

产品经理能力包已进一步沉淀为 Codex skill：

```text
/Users/alpha/.codex/skills/product-manager-kit/
```

该 skill 的参考资料来自：

```text
14-exports/product-manager-kit/
```

## 可选方向

### 方向 A：继续推进当前项目

- 价值：可以用真实或模拟任务验证 `product-manager-kit` skill 是否能被正确触发并完成产品经理任务。
- 风险：如果不验证，skill 可能存在路由说明过宽、过窄或执行材料读取不足的问题。
- 建议：下一步在新对话或其他项目中使用一个真实产品任务验证 skill。

### 方向 B：先补输入或上下文

- 价值：可以明确产品经理能力包是给自己、团队成员还是外部协作者使用。
- 风险：当前包已可用于第一轮验证，不必等待定位完全细化。
- 建议：验证后再决定是否拆轻量版和完整版。

### 方向 C：暂停并沉淀

- 价值：当前导出工作流和 product-manager-kit 已完成第一版沉淀。
- 风险：缺少真实使用反馈。
- 建议：可以暂停，但建议后续补一个独立使用验证案例。

## 推荐下一步

已完成：

```text
14-exports/product-manager-kit/
```

推荐下一步：

```text
请在新对话或其他项目中输入一个真实产品需求，验证 product-manager-kit skill 是否会正确触发，并观察它是否能正确选择 workflow、template 和 scorecard。
```

更快的验证入口：

```text
请使用 14-exports/product-manager-kit/START-HERE.md 里的“一句话启动”进行验证。
```

自动读取验证入口：

```text
请参考 14-exports/product-manager-kit/START-HERE.md 里的“外部自动读取配置”，在新项目根目录创建 AI-WORKFLOW-RULES.md 后，用一句自然语言产品需求测试是否会自动触发 product-manager-kit。
```

## 待确认问题

- 产品经理能力包是给自己使用，还是给其他人使用。
- 是否需要补充脱敏后的真实案例。
- 是否需要做轻量版和完整版两个版本。
