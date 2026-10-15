#!/usr/bin/env python3
"""Install WorkflowProject capability kits into an external code project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "14-exports"

KIT_ALIASES = {
    "governance": "project-governance-kit",
    "project-governance": "project-governance-kit",
    "team": "team-orchestration-kit",
    "orchestration": "team-orchestration-kit",
    "product": "product-manager-kit",
    "product-manager": "product-manager-kit",
    "ui": "ui-designer-kit",
    "ui-designer": "ui-designer-kit",
    "developer": "developer-kit",
    "dev": "developer-kit",
    "tester": "tester-kit",
    "test": "tester-kit",
}

DEFAULT_KITS = [
    "project-governance-kit",
    "team-orchestration-kit",
    "product-manager-kit",
    "ui-designer-kit",
    "developer-kit",
    "tester-kit",
]

AGENTS_CONTENT = """# AI 开发协作规则

本项目已接入 WorkflowProject 能力包。

开始任何产品、UI、开发或测试任务前，先阅读：

```text
.ai/kits/project-governance-kit/START-HERE.md
```

默认先执行项目治理检查：

1. 检查项目架构、模块边界和现有项目规则。
2. 检查设计规范、组件状态和设备适配要求。
3. 检查任务列表、模块文档、测试规则和项目记忆。
4. 缺少关键材料时先列出缺口并询问用户。
5. 材料齐全后先形成整体规划和任务列表。
6. 一次只执行一条任务，完成后立即验证。
7. 根据实际需要调用团队总调度或具体角色能力。
8. 代码、测试和项目文档发生变化时检查同步。

默认能力顺序：

```text
project-governance-kit
-> team-orchestration-kit（需要跨角色时）
-> product-manager-kit / ui-designer-kit / developer-kit / tester-kit（按需）
```

不得为了形式完整而强制所有角色参与，也不得把 AI 推断当成已确认的项目事实。
"""

CURSOR_RULE = """---
description: WorkflowProject 项目级治理规则，开发前检查架构、模块、设计规范和任务状态
alwaysApply: true
---

开始任务前，先阅读：

```text
.ai/kits/project-governance-kit/START-HERE.md
```

默认执行：

项目治理检查 -> 架构和模块检查 -> 设计规范检查 -> 整体规划 -> 任务列表 -> 逐条实现 -> 逐条验证 -> 文档同步

缺少架构、模块边界、设计规范或任务列表时，先列出缺口并与用户确认，不要直接大范围修改代码。

根据任务需要调用：

- team-orchestration-kit
- product-manager-kit
- ui-designer-kit
- developer-kit
- tester-kit
"""


def parse_kits(value: str) -> list[str]:
    if value.strip().lower() == "all":
        return DEFAULT_KITS.copy()

    result = []
    for raw_name in value.split(","):
        name = raw_name.strip().lower()
        if not name:
            continue
        resolved = KIT_ALIASES.get(name, name)
        if resolved not in result:
            result.append(resolved)
    return result


def write_text(path: Path, content: str, force: bool, dry_run: bool, created: list[str], skipped: list[str]) -> None:
    if path.exists() and not force:
        skipped.append(f"已存在，未覆盖：{path}")
        return
    if dry_run:
        created.append(f"将写入：{path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    created.append(str(path))


def install(args: argparse.Namespace) -> int:
    project = Path(args.project).expanduser().resolve()
    selected = parse_kits(args.kits)
    missing = [name for name in selected if not (EXPORTS / name).is_dir()]
    if missing:
        print("找不到能力包：" + ", ".join(missing))
        return 2

    created: list[str] = []
    skipped: list[str] = []
    kits_dir = project / ".ai" / "kits"

    print(f"目标项目：{project}")
    print("准备安装：" + ", ".join(selected))
    if args.dry_run:
        print("模式：预览，不写入文件")

    if not args.dry_run:
        project.mkdir(parents=True, exist_ok=True)

    for kit_name in selected:
        source = EXPORTS / kit_name
        destination = kits_dir / kit_name
        if destination.exists() and not args.force:
            skipped.append(f"已存在，未覆盖：{destination}")
            continue
        if args.dry_run:
            created.append(f"将复制：{source} -> {destination}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        created.append(str(destination))

    if not args.no_agents:
        write_text(project / "AGENTS.md", AGENTS_CONTENT, args.force, args.dry_run, created, skipped)

    if not args.no_rules:
        write_text(project / "AI-WORKFLOW-RULES.md", AGENTS_CONTENT, args.force, args.dry_run, created, skipped)
        write_text(
            project / ".cursor" / "rules" / "project-governance.workflowproject.mdc",
            CURSOR_RULE,
            args.force,
            args.dry_run,
            created,
            skipped,
        )

    print("\n已创建或准备创建：")
    for item in created:
        print(f"- {item}")

    if skipped:
        print("\n已跳过：")
        for item in skipped:
            print(f"- {item}")
        print("\n已有规则不会被覆盖，请人工合并新增规则内容。")

    print("\n安装完成后的启动方式：")
    print("请先做项目治理检查，再处理我的任务：{写下你的任务}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="把 WorkflowProject 能力包安装到外部代码项目")
    parser.add_argument("project", help="目标代码项目路径")
    parser.add_argument(
        "--kits",
        default="all",
        help="安装 all，或逗号分隔的 governance,team,product,ui,developer,tester",
    )
    parser.add_argument("--dry-run", action="store_true", help="只预览，不写入文件")
    parser.add_argument("--force", action="store_true", help="覆盖同名能力包和规则文件")
    parser.add_argument("--no-agents", action="store_true", help="不生成 AGENTS.md")
    parser.add_argument("--no-rules", action="store_true", help="不生成 AI-WORKFLOW-RULES.md 和 Cursor 规则")
    return parser


if __name__ == "__main__":
    raise SystemExit(install(build_parser().parse_args()))
