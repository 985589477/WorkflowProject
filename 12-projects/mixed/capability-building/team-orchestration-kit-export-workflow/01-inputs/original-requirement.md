# 原始需求

## 用户输入

```text
我现在需要提供一个这个混合角色总入口的导出，用来给别的项目使用
```

## 需求理解

用户需要把当前 WorkflowProject 中的跨角色团队总调度能力导出为独立能力包，让其他项目也能使用。

这个导出包不是替代产品经理、UI 设计师、开发工程师、测试工程师四个角色包，而是作为团队总入口：

- 判断任务是否跨角色。
- 判断哪些角色参与。
- 判断谁先接管。
- 负责角色之间交接检查。
- 负责开发交付后的产品/UI/测试验收判断。
- 出现协作阻塞时输出 badcase 回流建议。

## 导出目标

```text
14-exports/team-orchestration-kit/
```

## 依赖关系

建议与以下能力包同级放置：

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```
