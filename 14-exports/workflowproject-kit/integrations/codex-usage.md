# Codex 接入

## 作为 Skill

把整个 `workflowproject-kit` 目录复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，重启 Codex 后即可由 `SKILL.md` 作为统一入口使用。

## 作为项目治理规则

在目标项目中执行：

```bash
python3 workflowproject-kit/scripts/install_project.py .
```

这会生成项目级 `AGENTS.md`，适合让规则跟着项目走。

## 使用示例

```text
请使用 WorkflowProject 检查当前项目，先给出开发规划，再按任务列表逐条实现：增加用户头像上传功能。
```
