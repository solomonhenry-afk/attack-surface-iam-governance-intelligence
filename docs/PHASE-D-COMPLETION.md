# Phase D Completion — Identity Risk Scoring and Blast-Radius Analytics

## Status

Completed.

## Deliverables Produced

- `docs/PHASE-D-IDENTITY-RISK-SCORING-AND-BLAST-RADIUS-ANALYTICS.md`
- `scripts/score_iam_risk.py`
- `output/iam_risk_register.json`

## Methodology Applied

Each IAM exposure finding was scored using:

- Likelihood
- Impact
- Control effectiveness
- Confidence
- Blast radius
- Residual risk rating

## Governance Outcome

The IAM risk register ranks exposure findings by residual risk and provides a prioritized remediation queue. This gives Phase E a defensible basis for control mapping, treatment decisions, ownership, and remediation tracking.

## Evidence

- Successful execution of `python3 scripts/score_iam_risk.py`
- Terminal view of the prioritized IAM risk register
- `output/iam_risk_register.json`
