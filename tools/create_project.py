import argparse
import re
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "12-projects"
TEMPLATE_DIR = PROJECTS_DIR / "project-template"
ALLOWED_ROLES = {
    "mixed",
    "product-manager",
    "developer",
    "ui-designer",
    "tester",
    "researcher",
    "marketer",
}
ALLOWED_TYPES = {
    "capability-building",
    "real-cases",
    "experiments",
}


def slugify(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def write_readme(project_dir, role, project_type, name, title):
    readme = project_dir / "README.md"
    content = f"""# {title}

状态: draft
角色: {role}
项目类型: {project_type}
创建日期: {date.today().isoformat()}

## 目标

说明这个项目要解决什么问题。

## 角色

说明本项目主要使用的 AI 协作角色。

## 输入材料

说明输入资料来自哪里，具体材料放在 `01-inputs/`。

## 使用的工作流

列出本项目准备使用的工作流。

## 使用的模板

列出本项目准备使用或生成的模板。

## 当前状态

记录当前项目进度。

## 如何启动

下次继续本项目时，先阅读：

```text
README.md
00-progress/memory-summary.md
00-progress/next-actions.md
```

然后对 AI 说：

```text
请继续推进这个项目，并先说明当前状态、推荐下一步和会使用哪些文件。
```

## 进度记录

关键执行节点记录到：

```text
00-progress/progress-log.md
```

当前项目状态摘要记录到：

```text
00-progress/memory-summary.md
```

如果项目持续迭代很多轮，优先更新 `memory-summary.md`，不要让 AI 每次读取所有历史记录。

## 沉淀与提升

项目结束时记录哪些内容提升到全局模板、案例、知识库或评估体系。
"""
    readme.write_text(content, encoding="utf-8")


def write_progress_log(project_dir, title):
    progress_dir = project_dir / "00-progress"
    progress_dir.mkdir(exist_ok=True)
    progress_file = progress_dir / "progress-log.md"
    content = f"""# 进度记录

## {date.today().isoformat()}

- 当前阶段：项目已创建
- 调度角色：项目创建脚本
- 使用工作流：04-workflows/common/project-execution-workflow.md
- 使用模板：12-projects/project-template/
- 输入位置：未放入
- 输出位置：{project_dir.relative_to(ROOT)}
- 当前结果：已创建项目《{title}》
- 下一步：把原始材料放入 01-inputs/
"""
    progress_file.write_text(content, encoding="utf-8")


def write_decision_log(project_dir):
    progress_dir = project_dir / "00-progress"
    progress_dir.mkdir(exist_ok=True)
    decision_file = progress_dir / "decision-log.md"
    if decision_file.exists():
        return
    content = """# 决策记录

## 使用说明

这里记录项目执行过程中重要决策的原因。

## 记录模板

```md
## 决策：{决策标题}

### 背景

### 决策

### 原因

### 影响

### 日期
```
"""
    decision_file.write_text(content, encoding="utf-8")


def write_next_actions(project_dir):
    progress_dir = project_dir / "00-progress"
    progress_dir.mkdir(exist_ok=True)
    next_actions_file = progress_dir / "next-actions.md"
    if next_actions_file.exists():
        return
    content = """# 下一步判断

## 当前项目状态

待填写。

## 可选方向

### 方向 A：继续推进当前项目

- 价值：
- 风险：
- 建议：

### 方向 B：先补输入或上下文

- 价值：
- 风险：
- 建议：

### 方向 C：暂停并沉淀

- 价值：
- 风险：
- 建议：

## 推荐下一步

待填写。

## 待确认问题

- 待填写。
"""
    next_actions_file.write_text(content, encoding="utf-8")


def write_memory_summary(project_dir, title):
    progress_dir = project_dir / "00-progress"
    progress_dir.mkdir(exist_ok=True)
    memory_file = progress_dir / "memory-summary.md"
    if memory_file.exists():
        return
    content = f"""# 项目记忆摘要

## 一句话定位

《{title}》项目的当前状态摘要。

## 当前目标

待填写。

## 当前阶段

项目已创建。

## 最近一次有效进展

已创建项目骨架。

## 已完成内容

- 已创建 `00-progress/` 到 `06-lessons/` 项目结构。

## 当前有效决策

| 决策 | 原因 | 影响 | 来源 |
| --- | --- | --- | --- |

## 已废弃方向

| 方向 | 废弃原因 | 替代方案 |
| --- | --- | --- |

## 关键风险与注意事项

| 风险 | 影响 | 处理方式 |
| --- | --- | --- |

## 当前可用资产

| 资产 | 位置 | 用途 |
| --- | --- | --- |

## 下一步

- 把原始材料放入 `01-inputs/`。
- 明确本项目要使用的角色、工作流和模板。

## 需要追溯时再读

| 文件 | 什么时候读 |
| --- | --- |
| `00-progress/progress-log.md` | 需要查看完整执行流水时。 |
| `00-progress/decision-log.md` | 需要追溯重要决策原因时。 |
"""
    memory_file.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="创建一个新的 WorkflowProject 任务项目。")
    parser.add_argument("role", help="项目角色目录，例如 mixed、developer、product-manager、ui-designer、tester")
    parser.add_argument("name", help="项目英文短名，例如 login-bug-fix")
    parser.add_argument("--type", default="real-cases", help="项目类型：capability-building、real-cases、experiments，默认 real-cases")
    parser.add_argument("--output", help="项目根目录路径。指定后直接在该路径创建项目内部结构，不再追加项目名。")
    parser.add_argument("--title", help="项目中文标题，默认使用项目短名")
    args = parser.parse_args()

    role = slugify(args.role)
    name = slugify(args.name)
    project_type = slugify(args.type)
    if role not in ALLOWED_ROLES:
        allowed = ", ".join(sorted(ALLOWED_ROLES))
        raise SystemExit(f"不支持的角色目录：{args.role}\n可选值：{allowed}")
    if project_type not in ALLOWED_TYPES:
        allowed = ", ".join(sorted(ALLOWED_TYPES))
        raise SystemExit(f"不支持的项目类型：{args.type}\n可选值：{allowed}")
    if not name:
        raise SystemExit("项目名不能为空。建议使用英文、数字和连字符。")
    if not TEMPLATE_DIR.exists():
        raise SystemExit(f"找不到项目模板目录：{TEMPLATE_DIR}")

    if args.output:
        target_dir = Path(args.output).expanduser()
        if not target_dir.is_absolute():
            target_dir = ROOT / target_dir
        target_dir = target_dir.resolve()
        try:
            target_dir.relative_to(ROOT)
        except ValueError as exc:
            raise SystemExit("项目根目录必须在当前 WorkflowProject 工作区内。") from exc
    else:
        target_dir = PROJECTS_DIR / role / project_type / name
    if target_dir.exists():
        raise SystemExit(f"项目已存在：{target_dir}")

    target_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        TEMPLATE_DIR,
        target_dir,
        ignore=shutil.ignore_patterns(".gitkeep"),
    )
    for child in ["00-progress", "01-inputs", "02-analysis", "03-prompts", "04-outputs", "05-review", "06-lessons"]:
        (target_dir / child).mkdir(exist_ok=True)

    title = args.title or name
    write_readme(target_dir, role, project_type, name, title)
    write_progress_log(target_dir, title)
    write_decision_log(target_dir)
    write_next_actions(target_dir)
    write_memory_summary(target_dir, title)

    print(f"已创建项目：{target_dir}")
    print("下一步：把原始材料或想法放入 01-inputs/，再阅读 00-system/quick-start.md。")


if __name__ == "__main__":
    main()
