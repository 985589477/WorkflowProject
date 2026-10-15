# 安装说明

## 推荐：安装到代码项目

```bash
python3 scripts/install_project.py /目标代码项目
```

先预览变更：

```bash
python3 scripts/install_project.py /目标代码项目 --dry-run
```

只有明确希望覆盖目标项目同名文件时才使用：

```bash
python3 scripts/install_project.py /目标代码项目 --force
```

## 作为 Codex Skill

把整个 `workflowproject-kit` 目录复制到：

```text
$CODEX_HOME/skills/workflowproject-kit/
```

没有设置 `CODEX_HOME` 时，通常使用：

```text
~/.codex/skills/workflowproject-kit/
```

复制后重启 Codex。Skill 的真正入口是根目录的 `SKILL.md`，不是 `README.md` 或 `START-HERE.md`。

## 注意

- 不需要把 WorkflowProject 全仓库复制到新项目。
- 不需要手工逐个复制六个角色包。
- 目标项目已有规则文件时，安装器默认保留原文件并报告跳过。
- 本包的 `kits/` 是由源包生成的随包资源，更新能力后应在源项目重新导出。
