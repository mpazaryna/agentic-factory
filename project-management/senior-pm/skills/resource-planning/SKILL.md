---
name: resource-planning
description: "Resource capacity planning and optimization with utilization modeling, skill matching, bottleneck identification, and what-if scenario analysis. Use when a user needs team capacity planning, resource allocation, utilization reports, skill gap analysis, or workforce planning for enterprise portfolios."
---

# Resource Capacity Planning

Portfolio-level resource analysis with utilization optimization, skill-based allocation, bottleneck identification, and scenario planning. Produces capacity reports with actionable reallocation recommendations.

## Usage

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/resource_capacity_planner.py <portfolio_data.json>
```

For sample data, use: `${CLAUDE_SKILL_DIR}/../shared/assets/sample_project_data.json`

## Capacity Analysis Framework

- **Utilization Optimization**: Target 70-85% for sustainable productivity
- **Skill Matching**: Algorithm-based resource allocation to maximize efficiency
- **Bottleneck Identification**: Critical path resource constraints across portfolio
- **Scenario Planning**: What-if analysis for resource reallocation strategies

## Key Thresholds

| Utilization | Status | Action |
|---|---|---|
| >90% | Over-allocated | Immediate reallocation needed |
| 75-85% | Optimal | Maintain current allocation |
| 60-75% | Under-utilized | Consider cross-project assignment |
| <60% | Significantly under | Flag for reallocation discussion |

## Assessment Workflow

1. Run capacity planner against current portfolio data
2. If any team utilization >90% or <60%, flag for immediate reallocation discussion
3. Identify skill gaps and bottlenecks across portfolio
4. Run what-if scenarios for proposed changes
5. Generate optimization recommendations

## Quarterly Planning

1. **Analyze capacity constraints** across upcoming quarter
2. **Plan resource reallocation** and hiring strategies
3. **Identify skill gaps** and training needs
4. **Model scenarios** for new initiatives and sunset decisions

## Integration with Health & Risk

- Feed utilization data into portfolio health scoring (resource dimension)
- Use risk analysis outputs to identify resource-related risks
- Align capacity plans with prioritization model outputs

## KPIs

- Resource Utilization: 75-85% average across portfolio
- Skill Coverage: >90% of critical skills covered by 2+ team members
- Allocation Accuracy: <10% variance from planned allocation
- Time-to-Fill: <30 days for critical resource gaps
