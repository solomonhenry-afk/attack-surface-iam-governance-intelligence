# Methodology — Task 3 IAM Governance Intelligence

## Risk Scoring

Each IAM finding is evaluated using five dimensions:

| Dimension | Purpose |
|---|---|
| Likelihood | Probability that an exposure could be abused |
| Impact | Consequence if the exposure is exploited |
| Control Effectiveness | Strength of existing controls |
| Confidence | Reliability of supporting evidence |
| Blast Radius | Scope of potentially affected identities and assets |

```text
Inherent Risk = Likelihood × Impact

Residual Risk = Inherent Risk × (1 - Control Effectiveness / 5)
                + Blast Radius Adjustment
