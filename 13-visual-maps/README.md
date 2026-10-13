# 可视化导图

这里统一存放项目生成的 XMind 导图和对应 Markdown 大纲。

## 当前导图

- `WorkflowProject.xmind`：项目框架总览导图。
- `WorkflowProject-mindmap-outline.md`：项目框架总览 Markdown 大纲。
- `WorkflowProject-operation-flow.xmind`：从材料到输出的操作流程导图。
- `WorkflowProject-operation-flow-outline.md`：操作流程 Markdown 大纲。
- `WorkflowProject-file-responsibility.xmind`：当前文件与职责导图，由脚本自动扫描当前目录生成。
- `WorkflowProject-file-responsibility-outline.md`：当前文件与职责 Markdown 大纲，由脚本自动扫描当前目录生成。

## 生成脚本

导图由 `tools/` 下的脚本生成：

- `tools/generate_xmind.py`
- `tools/generate_operation_flow_xmind.py`
- `tools/generate_file_responsibility_xmind.py`

其中 `generate_file_responsibility_xmind.py` 会自动扫描当前项目目录。新增、删除或移动文件后，重新运行该脚本即可刷新文件职责图。

## 刷新导图

推荐使用：

```bash
python3 tools/refresh_maps.py
```

也可以分别运行：

```bash
python3 tools/generate_xmind.py
python3 tools/generate_operation_flow_xmind.py
python3 tools/generate_file_responsibility_xmind.py
```
