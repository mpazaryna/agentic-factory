---
name: portfolio-health
description: "Assess portfolio health across multiple dimensions with RAG status, trend analysis, and executive recommendations. Use when reviewing project portfolios, building health dashboards, tracking milestone progress, or preparing executive status reports."
---

# Portfolio Health Assessment

Comprehensive multi-dimensional health scoring for enterprise project portfolios. Runs analysis scripts against portfolio data to produce RAG status, intervention priorities, and executive recommendations.

## Usage

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/project_health_dashboard.py <portfolio_data.json>
```

For sample data, use: `${CLAUDE_SKILL_DIR}/../shared/assets/sample_project_data.json`

## Health Dimensions (Weighted Scoring)

- **Timeline Performance** (25%): Schedule adherence, milestone achievement, critical path analysis
- **Budget Management** (25%): Spend variance, forecast accuracy, cost efficiency metrics
- **Scope Delivery** (20%): Feature completion rates, requirement satisfaction, change control
- **Quality Metrics** (20%): Code coverage, defect density, technical debt, security posture
- **Risk Exposure** (10%): Risk score, mitigation effectiveness, exposure trends

## RAG Status Calculation

- 🟢 Green: Composite score >80, all dimensions >60
- 🟡 Amber: Composite score 60-80, or any dimension 40-60
- 🔴 Red: Composite score <60, or any dimension <40

## Weekly Review Workflow

1. **Data Collection & Validation**
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/scripts/project_health_dashboard.py current_portfolio.json
   ```
   If any project composite score <60 or a critical data field is missing, STOP and resolve data integrity issues before proceeding.

2. **Synthesize into Executive Summary**
   - Highlight critical issues and recommendations
   - Include trend analysis (improving/declining/stable)
   - Prepare stakeholder communications

## KPIs

Reference: [portfolio-kpis.md](references/portfolio-kpis.md) for full definitions.

- On-time Delivery Rate: >80% within 10% of planned timeline
- Budget Variance: <5% average across portfolio
- Quality Score: >85 composite rating
- Resource Utilization: 75-85% average

## Templates

- Executive report: [executive_report_template.md](../shared/assets/executive_report_template.md)
- Project charter: [project_charter_template.md](../shared/assets/project_charter_template.md)
- RACI matrix: [raci_matrix_template.md](../shared/assets/raci_matrix_template.md)

## Prioritization Models

When reprioritizing based on health scores, apply the appropriate model:

- **WSJF**: Resource-constrained agile portfolios with quantifiable cost-of-delay
- **RICE**: Customer-facing initiatives where reach metrics are quantifiable
- **ICE**: Rapid prioritization during brainstorming or when analysis time is limited
- **MoSCoW**: Multiple stakeholder groups with differing priorities

Reference: [portfolio-prioritization-models.md](../shared/portfolio-prioritization-models.md)
