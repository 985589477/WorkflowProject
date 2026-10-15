from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "12-projects" / "asset-index.md"

ROLE_LABELS = {
    "common": "通用能力",
    "meta": "Meta 能力",
    "product-manager": "产品经理",
    "developer": "开发工程师",
    "ui-designer": "UI 设计",
    "tester": "测试工程师",
    "researcher": "研究",
    "marketer": "市场营销",
}


def rel(path):
    return path.relative_to(ROOT).as_posix()


def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def read_title(path):
    for line in read_text(path).splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem


def first_paragraph(path):
    lines = read_text(path).splitlines()
    parts = []
    after_title = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            after_title = True
            continue
        if not after_title:
            continue
        if not stripped:
            if parts:
                break
            continue
        if stripped.startswith(("```", "## ", "- ", "| ")):
            if parts:
                break
            continue
        if stripped.startswith(("状态:", "版本:", "角色:", "导出时间：", "导出时间:")):
            continue
        parts.append(stripped)
        if len("".join(parts)) >= 90:
            break
    return " ".join(parts) if parts else "打开文件查看详细说明。"


def list_markdown(base, skip_readme=True):
    if not base.exists():
        return []
    files = sorted(base.glob("*.md"))
    if skip_readme:
        files = [path for path in files if path.name != "README.md"]
    return files


def role_from_parent(path):
    return path.parent.name


def workflow_items(role):
    base = ROOT / "04-workflows" / role
    return [
        {
            "title": read_title(path),
            "path": rel(path),
            "summary": first_paragraph(path),
            "usage": f"请参考 {rel(path)} 处理我的任务：{{写下你的任务或材料}}",
        }
        for path in list_markdown(base)
    ]


def template_items(role):
    base = ROOT / "06-templates" / role
    return [
        {
            "title": read_title(path),
            "path": rel(path),
            "summary": first_paragraph(path),
            "usage": f"请使用 {rel(path)} 作为输出模板，处理：{{写下你的任务或材料}}",
        }
        for path in list_markdown(base)
    ]


def kit_items():
    items = []
    for readme in sorted((ROOT / "14-exports").glob("*-kit/README.md")):
        kit_dir = readme.parent
        name = kit_dir.name
        items.append(
            {
                "title": read_title(readme),
                "name": name,
                "path": rel(kit_dir),
                "entry": rel(kit_dir / "START-HERE.md"),
                "summary": first_paragraph(readme),
                "usage": f"请使用 {name} 处理我的任务：{{写下你的任务或材料}}",
            }
        )
    return items


def scorecard_items():
    base = ROOT / "11-evaluations" / "output-scorecards"
    return [
        {
            "title": read_title(path),
            "path": rel(path),
            "summary": first_paragraph(path),
            "usage": f"请使用 {rel(path)} 评审这份输出：{{粘贴或指向输出文档}}",
        }
        for path in list_markdown(base)
    ]


def standard_items():
    base = ROOT / "05-standards"
    files = list_markdown(base)
    files.extend(sorted((base / "quality-checklists").glob("*.md")))
    return [
        {
            "title": read_title(path),
            "path": rel(path),
            "summary": first_paragraph(path),
            "usage": f"请按 {rel(path)} 检查或约束当前工作。",
        }
        for path in files
    ]


def tool_items():
    base = ROOT / "tools"
    return [
        {
            "title": path.name,
            "path": rel(path),
            "summary": script_summary(path),
            "usage": f"python3 {rel(path)}",
        }
        for path in sorted(base.glob("*.py"))
    ]


def script_summary(path):
    mapping = {
        "create_project.py": "创建标准项目目录和 00-06 执行结构。",
        "generate_project_index.py": "刷新项目索引，帮助判断项目职责、状态和启动方式。",
        "generate_asset_index.py": "刷新可用资产索引，帮助按能力查找角色包、工作流、模板和评分表。",
        "generate_dashboard_data.py": "刷新 React 可视化控制台使用的数据。",
        "refresh_maps.py": "一键刷新项目索引、资产索引、控制台数据和 XMind 导图。",
    }
    return mapping.get(path.name, "项目维护脚本，打开文件查看具体用途。")


def write_items(lines, items, show_entry=False):
    if not items:
        lines.extend(["暂无。", ""])
        return
    for item in items:
        lines.extend(
            [
                f"### {item['title']}",
                "",
                f"- 路径：`{item['path']}`",
            ]
        )
        if show_entry:
            lines.append(f"- 入口：`{item['entry']}`")
        lines.extend(
            [
                f"- 作用：{item['summary']}",
                "- 使用示例：",
                "",
                "```text",
                item["usage"],
                "```",
                "",
            ]
        )


def write_role_section(lines, role):
    label = ROLE_LABELS.get(role, role)
    workflows = workflow_items(role)
    templates = template_items(role)
    if not workflows and not templates:
        return

    lines.extend([f"## {label}", ""])
    if workflows:
        lines.extend(["### 工作流", ""])
        for item in workflows:
            lines.extend(
                [
                    f"- `{item['path']}`：{item['title']}。{item['summary']}",
                ]
            )
        lines.append("")
    if templates:
        lines.extend(["### 模板", ""])
        for item in templates:
            lines.extend(
                [
                    f"- `{item['path']}`：{item['title']}。{item['summary']}",
                ]
            )
        lines.append("")


def main():
    lines = [
        "# 可用资产索引",
        "",
        "本文件由 `tools/generate_asset_index.py` 自动生成，用来回答：当前 WorkflowProject 里有哪些能力可以直接使用。",
        "",
        "它和 `12-projects/project-index.md` 的区别：",
        "",
        "- `project-index.md` 看具体项目：项目是怎么来的、现在到哪一步、下次怎么继续。",
        "- `asset-index.md` 看可复用资产：现在有哪些角色包、工作流、模板、评分表、标准和脚本可以调用。",
        "",
        "刷新方式：",
        "",
        "```bash",
        "python3 tools/generate_asset_index.py",
        "```",
        "",
        "如果要同时刷新项目索引、控制台数据和 XMind，运行：",
        "",
        "```bash",
        "python3 tools/refresh_maps.py",
        "```",
        "",
        "## 先用哪个",
        "",
        "| 场景 | 推荐入口 |",
        "| --- | --- |",
        "| 不知道该用哪个产品能力 | `14-exports/product-manager-kit/START-HERE.md` |",
        "| 不知道该用哪个开发能力 | `14-exports/developer-kit/START-HERE.md` |",
        "| 想继续某个历史项目 | `12-projects/project-index.md` |",
        "| 想找某个工作流或模板 | 本文件对应章节 |",
        "| 想刷新全局视图 | `python3 tools/refresh_maps.py` |",
        "",
        "## 角色能力包",
        "",
    ]

    write_items(lines, kit_items(), show_entry=True)

    for role in ["product-manager", "developer", "ui-designer", "tester", "common", "meta", "researcher", "marketer"]:
        write_role_section(lines, role)

    lines.extend(["## 评分表", ""])
    write_items(lines, scorecard_items())

    lines.extend(["## 标准和检查清单", ""])
    write_items(lines, standard_items())

    lines.extend(["## 工具脚本", ""])
    write_items(lines, tool_items())

    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"已生成：{rel(OUTPUT)}")


if __name__ == "__main__":
    main()
