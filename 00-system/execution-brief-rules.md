# 执行前说明规则

## 目的

在 AI 执行任务前，先让用户知道 AI 准备做什么、为什么做、会影响哪些文件。

## 适用范围

适用于所有项目执行、框架变更、模板生成、案例沉淀和脚本修改任务。

## 执行前必须说明

每次开始关键操作前，AI 应输出一段简短说明：

```text
当前目标：
我要做什么：
为什么要做：
会使用哪些文件：
会调度哪个角色：
会使用哪个工作流：
预计产出什么：
完成后你需要看哪里：
```

## 使用要求

- 说明要短，避免变成另一份长文档。
- 如果只是简单问答，可以不写完整卡片。
- 如果涉及新增、修改、沉淀、评审、脚本执行，必须说明。
- 如果用户明确要求直接执行，也至少用一句话说明当前动作。

## 示例

```text
当前目标：把 bootstrap 项目沉淀为正式案例。
我要做什么：整理 input、workflow、template、prompt、output、review、lessons 和 progress。
为什么要做：让这个项目从工作现场升级为可复用案例。
会使用哪些文件：12-projects/mixed/capability-building/workflowproject-framework-bootstrap/。
会调度哪个角色：AI 案例库编辑。
会使用哪个工作流：example-extraction-workflow。
预计产出：09-examples/cross-functional/workflowproject-framework-bootstrap/。
完成后你需要看：案例 README 和 lessons。
```
