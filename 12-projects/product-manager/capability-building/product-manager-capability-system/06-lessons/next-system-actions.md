# 后续体系建设建议

## 推荐下一步

优先启动：

```bash
python3 tools/create_project.py product-manager requirement-analysis-workflow --type capability-building
```

原因：

需求分析是 PRD、功能规划、验收标准的上游能力。

## 第二步

启动：

```bash
python3 tools/create_project.py product-manager prd-workflow --type capability-building
```

原因：

PRD 是产品经理最核心、最常被复用的输出类型。

## 第三步

启动：

```bash
python3 tools/create_project.py product-manager acceptance-criteria-workflow --type capability-building
```

原因：

验收标准可以连接产品和开发，适合验证跨角色协作。

## 暂缓事项

暂缓一次性建设：

- 竞品分析。
- 用户反馈整理。
- 版本规划。
- 产品策略判断。

原因：

这些能力需要更多真实材料，适合后续在具体场景中验证。
