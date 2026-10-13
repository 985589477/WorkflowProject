# 后续建议

## 推荐下一步

用一个真实产品想法验证需求分析工作流。

建议创建：

```bash
python3 tools/create_project.py product-manager requirement-analysis-real-case --type real-cases
```

然后只提供一句真实产品想法，让流程从：

```text
想法转输入
-> 需求分析
-> 输出评审
```

跑一遍。

## 第二步

如果验证通过，再建设：

```bash
python3 tools/create_project.py product-manager prd-workflow --type capability-building
```

原因：

PRD 生成应建立在稳定的需求分析能力之上。
