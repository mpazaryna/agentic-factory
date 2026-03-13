---
name: risk-analysis
description: "Quantitative risk analysis with EMV calculations, Monte Carlo simulation inputs, risk matrices, and mitigation strategies. Use when a user needs risk assessments, risk registers, risk heat maps, mitigation planning, or portfolio risk correlation analysis for enterprise projects."
---

# Quantitative Risk Analysis

Risk quantification using Expected Monetary Value (EMV) analysis, probability/impact matrices, category-weighted scoring, and portfolio risk correlation. Produces risk matrices, mitigation strategies, and risk-adjusted budget recommendations.

## Usage

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/risk_matrix_analyzer.py <portfolio_data.json>
```

For sample data, use: `${CLAUDE_SKILL_DIR}/../shared/assets/sample_project_data.json`

## Risk Quantification Process

1. **Probability Assessment** (1-5 scale): Historical data, expert judgment, Monte Carlo inputs
2. **Impact Analysis** (1-5 scale): Financial, schedule, quality, and strategic impact vectors
3. **Category Weighting**: Technical (1.2x), Resource (1.1x), Financial (1.4x), Schedule (1.0x)
4. **EMV Calculation**:

```python
category_weights = {"Technical": 1.2, "Resource": 1.1, "Financial": 1.4, "Schedule": 1.0}
for risk in risks:
    score = risk["probability"] * risk["impact"] * category_weights[risk["category"]]
    emv = risk["probability"] * risk["financial_impact"]
```

## Risk Response Strategies (by score threshold)

- **Avoid** (>18): Eliminate through scope/approach changes
- **Mitigate** (12-18): Reduce probability or impact through active intervention
- **Transfer** (8-12): Insurance, contracts, partnerships
- **Accept** (<8): Monitor with contingency planning

## Three-Point Estimation for Monte Carlo

```python
def three_point_estimate(optimistic, most_likely, pessimistic):
    expected = (optimistic + 4 * most_likely + pessimistic) / 6
    std_dev = (pessimistic - optimistic) / 6
    return expected, std_dev
```

## Portfolio Risk Correlation

```python
def portfolio_risk(individual_risks, correlations):
    sum_sq = sum(r**2 for r in individual_risks)
    sum_corr = sum(2 * c * individual_risks[i] * individual_risks[j]
                   for i, j, c in correlations)
    return math.sqrt(sum_sq + sum_corr)
```

## Risk Appetite Framework

- **Conservative**: Risk scores 0-8, 25-30% contingency reserves
- **Moderate**: Risk scores 8-15, 15-20% contingency reserves
- **Aggressive**: Risk scores 15+, 10-15% contingency reserves

## Risk-Adjusted Budget

```python
def risk_adjusted_budget(base_budget, portfolio_risk_score, risk_tolerance_factor):
    risk_premium = portfolio_risk_score * risk_tolerance_factor
    return base_budget * (1 + risk_premium)
```

## Assessment Workflow

1. Run risk matrix analyzer against current portfolio data
2. If any risk score >18 (Avoid threshold), STOP and initiate escalation to project sponsor
3. Classify risks by category and assign response strategies
4. Calculate portfolio-level EMV and risk-adjusted budgets
5. Generate mitigation plans with owners and timelines

## Risk Classification Categories

- **Technical**: Architecture, integration, performance
- **Resource**: Availability, skills, retention
- **Schedule**: Dependencies, critical path, external factors
- **Financial**: Budget overruns, currency, economic factors
- **Business**: Market changes, competitive pressure, strategic shifts

Reference: [risk-management-framework.md](references/risk-management-framework.md) for full framework details.
