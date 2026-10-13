from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "12-projects"
OUTPUT = PROJECTS_DIR / "project-index.md"

ROLE_LABELS = {
    "mixed": "跨角色项目",
    "product-manager": "产品经理项目",
    "developer": "开发工程师项目",
    "ui-designer": "UI 设计项目",
    "researcher": "研究项目",
    "marketer": "市场营销项目",
}

ROLE_ORDER = [
    "mixed",
    "product-manager",
    "developer",
    "ui-designer",
    "researcher",
    "marketer",
]

TYPE_LABELS = {
    "capability-building": "能力建设项目",
    "real-cases": "真实使用项目",
    "experiments": "实验探索项目",
    "legacy": "未分型项目",
}

TYPE_ORDER = [
    "capability-building",
    "real-cases",
    "experiments",
    "legacy",
]


def rel(path):
    return path.relative_to(ROOT).as_posix()


def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def read_title(path):
    for line in read_text(path).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def read_field(path, field):
    prefix = f"{field}:"
    for line in read_text(path).splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return ""


def section_text(markdown, heading):
    lines = markdown.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == f"## {heading}":
            start = index + 1
            break
    if start is None:
        return ""

    collected = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        collected.append(line)
    return "\n".join(collected).strip()


def first_content_line(markdown, heading):
    content = section_text(markdown, heading)
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        if stripped.startswith("- "):
            return stripped[2:].strip()
        return stripped
    return "未填写"


def section_summary(markdown, heading, max_parts=3):
    content = section_text(markdown, heading)
    parts = []
    in_code = False
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        parts.append(stripped)
        if len(parts) >= max_parts and not in_code:
            break
    return " ".join(parts) if parts else "未填写"


def next_action(project_dir):
    content = read_text(project_dir / "00-progress" / "next-actions.md")
    result = section_summary(content, "推荐下一步", max_parts=5)
    if result != "未填写":
        return result
    readme = read_text(project_dir / "README.md")
    return first_content_line(readme, "当前状态")


def usage_example(item):
    path = item["path"]
    title = item["title"]
    role = item["role"]
    project_type = item["type"]

    if project_type == "capability-building":
        return "\n".join(
            [
                f"请使用 {path} 继续这个能力建设项目，",
                "并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。",
                "",
                "我想要优化或继续建设这个能力：",
                "{写你的想法或修改要求}",
                "",
                "请按项目流程更新 input、analysis、prompt、output、review 和 lessons。",
            ]
        )

    if project_type == "real-cases":
        return "\n".join(
            [
                f"请参考 {path} 的项目结构处理一个真实使用任务。",
                "",
                "我的想法是：",
                "{写你的真实需求或产品想法}",
                "",
                f"请输出到 12-projects/{role}/real-cases/{{项目名}}/，",
                "并把核心结果保存到对应的 02-analysis、04-outputs 或 05-review 目录。",
            ]
        )

    if project_type == "experiments":
        return "\n".join(
            [
                f"请使用 {path} 继续这个实验探索项目。",
                "",
                "我要验证的想法是：",
                "{写你的实验想法}",
                "",
                "请先说明实验目标、验证方式、输出位置和成功标准。",
            ]
        )

    return "\n".join(
        [
            f"请使用 {path} 继续这个项目，",
            "并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。",
        ]
    )


def project_items():
    items = []
    readmes = list(PROJECTS_DIR.glob("*/*/*/README.md"))
    readmes.extend(PROJECTS_DIR.glob("*/*/README.md"))
    for readme in sorted(set(readmes)):
        if "project-template" in readme.parts:
            continue
        project_dir = readme.parent
        relative_parts = project_dir.relative_to(PROJECTS_DIR).parts
        if len(relative_parts) >= 3:
            role, project_type = relative_parts[0], relative_parts[1]
        elif len(relative_parts) == 2:
            role, project_type = relative_parts[0], "legacy"
        else:
            continue
        content = read_text(readme)
        goal = first_content_line(content, "目标")
        items.append(
            {
                "title": read_title(readme),
                "role": role,
                "type": read_field(readme, "项目类型") or project_type,
                "state": read_field(readme, "状态") or "unknown",
                "path": rel(project_dir),
                "duty": first_content_line(content, "项目职责") if section_text(content, "项目职责") else goal,
                "use_when": section_summary(content, "何时使用", max_parts=4) if section_text(content, "何时使用") else "需要理解或继续这个项目时使用。",
                "deliverables": section_summary(content, "关键产物", max_parts=4) if section_text(content, "关键产物") else "查看项目 README、04-outputs、05-review 和 06-lessons。",
                "goal": goal,
                "current": first_content_line(content, "当前状态"),
                "next": next_action(project_dir),
                "start": f"请使用 {rel(project_dir)} 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。",
            }
        )
        items[-1]["usage_example"] = usage_example(items[-1])
    return items


def grouped_items(items):
    groups = {}
    for item in items:
        groups.setdefault(item["role"], {}).setdefault(item["type"], []).append(item)

    ordered_roles = [role for role in ROLE_ORDER if role in groups]
    ordered_roles.extend(sorted(role for role in groups if role not in ROLE_ORDER))
    result = []
    for role in ordered_roles:
        type_groups = groups[role]
        ordered_types = [project_type for project_type in TYPE_ORDER if project_type in type_groups]
        ordered_types.extend(sorted(project_type for project_type in type_groups if project_type not in TYPE_ORDER))
        result.append((role, [(project_type, type_groups[project_type]) for project_type in ordered_types]))
    return result


def write_index(items):
    lines = [
        "# 项目索引",
        "",
        "本文件由 `tools/generate_project_index.py` 自动生成，用来解决项目变多后不知道每个项目是干什么、从哪里继续的问题。",
        "",
        "刷新方式：",
        "",
        "```bash",
        "python3 tools/generate_project_index.py",
        "```",
        "",
        "如果要同时刷新可视化控制台和 XMind，运行：",
        "",
        "```bash",
        "python3 tools/refresh_maps.py",
        "```",
        "",
        "## 分组总览",
        "",
    ]

    if not items:
        lines.append("暂无项目。")
    else:
        for role, type_groups in grouped_items(items):
            role_label = ROLE_LABELS.get(role, role)
            role_total = sum(len(type_items) for _, type_items in type_groups)
            lines.extend(
                [
                    f"### {role_label}",
                    "",
                    f"- 角色目录：`12-projects/{role}/`",
                    f"- 项目数量：{role_total}",
                    "",
                ]
            )

            for project_type, type_items in type_groups:
                type_label = TYPE_LABELS.get(project_type, project_type)
                lines.extend(
                    [
                        f"#### {type_label}",
                        "",
                        f"- 项目类型：`{project_type}`",
                        f"- 项目数量：{len(type_items)}",
                        "",
                    ]
                )
                for item in type_items:
                    lines.extend(
                        [
                            f"##### {item['title']}",
                            "",
                            f"- 状态：{item['state']}",
                            f"- 路径：`{item['path']}`",
                            f"- 项目职责：{item['duty']}",
                            f"- 何时使用：{item['use_when']}",
                            f"- 关键产物：{item['deliverables']}",
                            f"- 目标：{item['goal']}",
                            f"- 当前状态：{item['current']}",
                            f"- 推荐下一步：{item['next']}",
                            "- 启动方式：",
                            "",
                            "```text",
                            item["start"],
                            "```",
                            "",
                            "- 使用示例：",
                            "",
                            "```text",
                            item["usage_example"],
                            "```",
                            "",
                        ]
                    )

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUTPUT)


def main():
    write_index(project_items())


if __name__ == "__main__":
    main()
