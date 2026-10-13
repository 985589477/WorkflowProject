# 可视化控制台

这是 WorkflowProject 的 React 可视化入口。

## 作用

用于快速理解：

- 当前项目状态。
- 已具备能力。
- 工作流主链路。
- 可复用资产。
- 模块分工。
- 当前风险。
- 下一步建议。

## 启动方式

```bash
cd 15-dashboard
npm install
npm run dev
```

## 数据刷新

控制台数据来自：

```text
15-dashboard/src/data.json
```

如果项目目录、案例、模板、工作流或工具脚本发生变化，运行：

```bash
python3 tools/generate_dashboard_data.py
```

如果希望同时刷新 XMind 导图和控制台数据，运行：

```bash
python3 tools/refresh_maps.py
```

## 当前版本

当前版本已经支持从项目目录自动生成基础数据。

后续可以增加：

- 项目详情页。
- 按角色筛选项目、案例和模板。
- 风险状态人工标记。
- 从进度日志中自动提取当前阶段。
