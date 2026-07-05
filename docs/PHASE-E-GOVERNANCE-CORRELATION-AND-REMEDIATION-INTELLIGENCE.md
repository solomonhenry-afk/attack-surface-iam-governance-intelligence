# Phase E — Governance Correlation and Remediation Intelligence

## Objective

Convert IAM risk findings into accountable remediation work that can be tracked, validated, and reported as governance evidence.

## Governance Workflow

```text
IAM finding → residual-risk score → control mapping → owner assignment
→ remediation action → validation evidence → residual-risk review

Lighthouse IAM Control Correlation
| Lighthouse Control | Control Objective                                                  | NIST CSF | CIS Controls | ISO/IEC 27001  |
| ------------------ | ------------------------------------------------------------------ | -------- | ------------ | -------------- |
| LT-IAM-001         | Privileged access is inventoried and monitored                     | PR.AA    | 5, 6         | A.5.15, A.5.18 |
| LT-IAM-002         | Dormant privileged accounts are identified and reviewed            | PR.AA    | 5            | A.5.16, A.5.18 |
| LT-IAM-003         | Service accounts have accountable owners and controlled privileges | PR.AA    | 5, 6         | A.5.16, A.5.18 |
| LT-IAM-004         | Privilege inheritance and toxic permissions are assessed           | PR.AA    | 5, 6         | A.5.15, A.8.2  |
| LT-IAM-005         | Identity attack paths are evaluated for blast-radius risk          | ID.RA    | 4, 5         | A.5.7, A.8.8   |
| LT-IAM-006         | IAM findings are mapped to remediation actions and reporting       | GV.RM    | 17           | A.5.35, A.5.36 |


Remediation Priority Rules
| Risk Rating | Target Treatment Window | Escalation                                       |
| ----------- | ----------------------: | ------------------------------------------------ |
| Critical    |                  7 days | Immediate security and infrastructure escalation |
| High        |                 30 days | Assigned owner and weekly review                 |
| Medium      |                 60 days | Monthly governance review                        |
| Low         |                 90 days | Routine control-improvement backlog              |

Deliverables:
-Governance-correlated remediation register
-Control and framework mappings
-Assigned remediation ownership
-Evidence and validation requirements
-Remediation priority summary
