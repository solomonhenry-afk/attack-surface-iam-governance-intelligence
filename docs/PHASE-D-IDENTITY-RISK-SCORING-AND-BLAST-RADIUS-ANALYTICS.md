# Phase D — Identity Risk Scoring and Blast-Radius Analytics

## Objective

Translate IAM exposure findings into a consistent, evidence-backed risk register that prioritizes remediation by residual risk and potential blast radius.

## Scoring Model

Each finding is scored on a 1–5 scale.

| Factor | Meaning |
|---|---|
| Likelihood | Probability that the exposure could be abused or lead to control failure |
| Impact | Business and security consequence if the exposure is exploited |
| Control Effectiveness | Strength of existing preventive, detective, and corrective controls |
| Confidence | Reliability and completeness of the supporting evidence |
| Blast Radius | Potential scope of systems, identities, and critical assets affected |

## Residual Risk Formula

```text
Inherent Risk = Likelihood × Impact

Control Reduction = Control Effectiveness / 5

Residual Risk = Inherent Risk × (1 - Control Reduction)
