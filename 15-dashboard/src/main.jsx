import React from "react";
import { createRoot } from "react-dom/client";
import {
  Activity,
  AlertTriangle,
  ArrowRight,
  Boxes,
  Brain,
  CheckCircle2,
  Compass,
  FileText,
  GitBranch,
  LayoutDashboard,
  Library,
  Map,
  PlayCircle,
  ShieldCheck,
  Sparkles,
  Waypoints
} from "lucide-react";
import dashboardData from "./data.json";
import "./styles.css";

const iconMap = {
  play: PlayCircle,
  brain: Brain,
  check: CheckCircle2,
  compass: Compass,
  library: Library,
  map: Map,
  boxes: Boxes
};

function Badge({ children, tone = "default" }) {
  return <span className={`badge ${tone}`}>{children}</span>;
}

const roleLabels = {
  mixed: "跨角色项目",
  "product-manager": "产品经理项目",
  developer: "开发工程师项目",
  "ui-designer": "UI 设计项目",
  researcher: "研究项目",
  marketer: "市场营销项目"
};

const roleOrder = ["mixed", "product-manager", "developer", "ui-designer", "researcher", "marketer"];
const typeLabels = {
  "capability-building": "能力建设项目",
  "real-cases": "真实使用项目",
  experiments: "实验探索项目",
  legacy: "未分型项目"
};
const typeOrder = ["capability-building", "real-cases", "experiments", "legacy"];

function App() {
  const {
    stats,
    capabilities,
    flow,
    assets,
    modules,
    risks,
    nextActions,
    projects,
    examples,
    updatedAt
  } = dashboardData;
  const projectGroups = roleOrder
    .filter((role) => projects.some((project) => project.role === role))
    .map((role) => ({
      role,
      label: roleLabels[role] || role,
      typeGroups: typeOrder
        .filter((type) => projects.some((project) => project.role === role && project.type === type))
        .map((type) => ({
          type,
          label: typeLabels[type] || type,
          items: projects.filter((project) => project.role === role && project.type === type)
        }))
    }));

  return (
    <main className="dashboard-shell">
      <aside className="sidebar" aria-label="控制台导航">
        <div className="brand">
          <LayoutDashboard size={22} />
          <div>
            <strong>WorkflowProject</strong>
            <span>AI 工作流控制台</span>
          </div>
        </div>
        <nav>
          <a href="#overview">总览</a>
          <a href="#capabilities">能力</a>
          <a href="#flow">流程</a>
          <a href="#assets">资产</a>
          <a href="#projects">项目</a>
          <a href="#risk">风险</a>
        </nav>
      </aside>

      <section className="content">
        <header className="hero" id="overview">
          <div>
            <p className="eyebrow">当前状态</p>
            <h1>从文件目录升级为可把控的 AI 工作流系统</h1>
            <p className="summary">
              这里汇总当前项目有什么、能用什么、风险在哪里，以及下一步应该如何推进。
            </p>
            <p className="data-source">{updatedAt}</p>
          </div>
          <div className="hero-action">
            <Badge tone="green">基础框架已完成</Badge>
            <Badge tone="blue">首个案例已沉淀</Badge>
          </div>
        </header>

        <section className="stats-grid" aria-label="项目指标">
          {stats.map((item) => (
            <article className={`stat-card ${item.tone}`} key={item.label}>
              <span>{item.label}</span>
              <strong>{item.value}</strong>
              <small>{item.detail}</small>
            </article>
          ))}
        </section>

        <section className="panel" id="capabilities">
          <div className="section-title">
            <Compass size={20} />
            <h2>能力地图</h2>
          </div>
          <div className="capability-grid">
            {capabilities.map(({ icon, title, path, status, note }) => {
              const Icon = iconMap[icon] || Sparkles;
              return (
              <article className="capability-card" key={path}>
                <div className="card-icon"><Icon size={19} /></div>
                <div>
                  <div className="card-head">
                    <h3>{title}</h3>
                    <Badge>{status}</Badge>
                  </div>
                  <p>{note}</p>
                  <code>{path}</code>
                </div>
              </article>
              );
            })}
          </div>
        </section>

        <section className="panel" id="flow">
          <div className="section-title">
            <Waypoints size={20} />
            <h2>流程地图</h2>
          </div>
          <div className="flow-row">
            {flow.map((step, index) => (
              <React.Fragment key={step}>
                <div className="flow-step">{step}</div>
                {index < flow.length - 1 && <ArrowRight className="flow-arrow" size={18} />}
              </React.Fragment>
            ))}
          </div>
          <div className="flow-note">
            <ShieldCheck size={18} />
            每个项目执行时同步记录 progress-log、decision-log 和 next-actions。
          </div>
        </section>

        <section className="two-column">
          <div className="panel" id="assets">
            <div className="section-title">
              <FileText size={20} />
              <h2>资产索引</h2>
            </div>
            <div className="asset-list">
              {assets.map((asset) => (
                <article className="asset-row" key={asset.path}>
                  <div>
                    <strong>{asset.title || asset.name}</strong>
                    <span>{asset.type}</span>
                    <code>{asset.path}</code>
                  </div>
                  <Badge tone={asset.state === "accepted" ? "green" : "default"}>{asset.state}</Badge>
                </article>
              ))}
            </div>
          </div>

          <div className="panel">
            <div className="section-title">
              <GitBranch size={20} />
              <h2>模块分工</h2>
            </div>
            <div className="module-list">
              {modules.map((module) => (
                <article className="module-row" key={module.scope}>
                  <strong>{module.name}</strong>
                  <code>{module.scope}</code>
                  <p>{module.duty}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="two-column" id="projects">
          <div className="panel">
            <div className="section-title">
              <Boxes size={20} />
              <h2>项目现场</h2>
            </div>
            <div className="asset-list">
              {projects.length === 0 && <p className="empty-text">暂无项目。</p>}
              {projectGroups.map((group) => (
                <div className="project-group" key={group.role}>
                  <div className="project-group-head">
                    <strong>{group.label}</strong>
                    <Badge>
                      {group.typeGroups.reduce((total, typeGroup) => total + typeGroup.items.length, 0)} 个项目
                    </Badge>
                  </div>
                  {group.typeGroups.map((typeGroup) => (
                    <div className="project-type-group" key={`${group.role}-${typeGroup.type}`}>
                      <div className="project-type-head">
                        <span>{typeGroup.label}</span>
                        <Badge>{typeGroup.items.length} 个</Badge>
                      </div>
                      {typeGroup.items.map((project) => (
                        <article className="asset-row" key={project.path}>
                          <div>
                            <strong>{project.title}</strong>
                            <span>{project.role} / {project.type}</span>
                            <p>{project.duty}</p>
                            <span>何时使用：{project.useWhen}</span>
                            <span>关键产物：{project.deliverables}</span>
                            <p>{project.goal}</p>
                            <span>下一步：{project.next}</span>
                            <code>{project.path}</code>
                          </div>
                          <Badge tone={project.state === "accepted" ? "green" : "default"}>{project.state}</Badge>
                        </article>
                      ))}
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </div>

          <div className="panel">
            <div className="section-title">
              <Library size={20} />
              <h2>正式案例</h2>
            </div>
            <div className="asset-list">
              {examples.length === 0 && <p className="empty-text">暂无案例。</p>}
              {examples.map((example) => (
                <article className="asset-row" key={example.path}>
                  <div>
                    <strong>{example.title}</strong>
                    <span>{example.type}</span>
                    <code>{example.path}</code>
                  </div>
                  <Badge tone={example.state === "accepted" ? "green" : "default"}>{example.state}</Badge>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="two-column">
          <div className="panel" id="risk">
            <div className="section-title">
              <AlertTriangle size={20} />
              <h2>风险把控</h2>
            </div>
            <div className="risk-list">
              {risks.map((risk) => (
                <article className="risk-row" key={risk.title}>
                  <Badge tone={risk.level === "低" ? "green" : "amber"}>{risk.level}</Badge>
                  <div>
                    <strong>{risk.title}</strong>
                    <p>{risk.action}</p>
                  </div>
                </article>
              ))}
            </div>
          </div>

          <div className="panel">
            <div className="section-title">
              <Sparkles size={20} />
              <h2>下一步建议</h2>
            </div>
            <div className="next-list">
              {nextActions.map((item) => (
                <article className="next-row" key={item.title}>
                  <Badge tone={item.title === "推荐" ? "blue" : "default"}>{item.title}</Badge>
                  <div>
                    <strong>{item.text}</strong>
                    <p>{item.reason}</p>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <footer>
          <Activity size={16} />
          数据来自 `15-dashboard/src/data.json`，可通过 `python3 tools/generate_dashboard_data.py` 刷新。
        </footer>
      </section>
    </main>
  );
}

export default App;

createRoot(document.getElementById("root")).render(<App />);
