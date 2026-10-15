# WorkflowProject 统一能力包

这是从 WorkflowProject 导出的可携带开发治理包。它把项目治理、跨角色调度、产品、UI、开发和测试能力放在一个 Skill 目录中，适合复制到其他代码项目后直接安装。

这个包不是另一套需要手工维护的文档。它由 WorkflowProject 的六个独立导出包生成，源项目中的能力更新后重新导出即可。

## 一句话安装

在目标项目外执行：

```bash
python3 /路径/workflowproject-kit/scripts/install_project.py /目标代码项目
```

安装器会把能力复制到目标项目的 `.ai/kits/`，并生成或补充：

- `AGENTS.md`
- `AI-WORKFLOW-RULES.md`
- `.cursor/rules/workflowproject-governance.mdc`

已有同名文件默认不会覆盖。确认要覆盖时再加 `--force`。

## Codex 使用

本目录本身就是一个可识别的 Codex Skill，入口是 `SKILL.md`。如果要作为个人全局 Skill 使用，把整个目录复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，然后重启 Codex。

如果只想约束某个代码项目，优先运行上面的项目安装器；这样能力和规则会跟着项目走，不依赖个人机器的全局配置。

## Cursor 使用

运行安装器后，Cursor 会通过目标项目的 `.cursor/rules/workflowproject-governance.mdc` 读取项目级规则。能力正文保存在 `.ai/kits/`，可随代码项目一起提交和评审。

## 统一入口

安装后可以直接对 AI 说：

```text
请使用 WorkflowProject 先检查当前项目，再规划并执行这个需求：{需求}
```

总入口会先检查项目事实和缺口，再决定是否调度产品、UI、开发或测试能力，不会为了形式强制所有角色参与。
