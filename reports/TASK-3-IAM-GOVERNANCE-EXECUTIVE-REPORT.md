# Executive IAM Governance Report

## Lighthouse Technology
### Domain 4 — Enterprise GRC Intelligence, Risk Analytics & Cyber Resilience Engineering
### Task 3 — Attack-Surface & IAM Governance Intelligence

**Generated:** 2026-07-05 16:46 UTC

> **Training-data notice:** This report is generated from a synthetic identity and privilege graph. It demonstrates an evidence-driven governance workflow and does not represent live enterprise findings.

## Executive Summary

- **IAM risks scored:** 12
- **Highest residual risk:** 18.0
- **Risk distribution:** {'critical': 3, 'high': 4, 'medium': 4, 'low': 1}
- **Blast-radius distribution:** {'5': 3, '3': 3, '2': 3, '4': 1, '1': 2}

## Top Prioritized IAM Risks

| Priority | Risk ID | Subject | Rating | Residual Risk | Blast Radius |
|---:|---|---|---|---:|---:|
| 1 | RISK-007 | svc_backup | CRITICAL | 18.0 | 5 |
| 2 | RISK-008 | svc_backup | CRITICAL | 18.0 | 5 |
| 3 | RISK-012 | svc_backup | CRITICAL | 18.0 | 5 |
| 4 | RISK-011 | Server Admins | HIGH | 15.0 | 3 |
| 5 | RISK-009 | svc_reporting | HIGH | 13.5 | 2 |

## Governance and Remediation Coverage

| Remediation ID | Owner | Lighthouse Control | Treatment Window | Status |
|---|---|---|---:|---|
| REM-007 | Infrastructure Engineering | LT-IAM-003 | 7 days | OPEN |
| REM-008 | Infrastructure Engineering | LT-IAM-003 | 7 days | OPEN |
| REM-012 | Identity and Access Management | LT-IAM-005 | 7 days | OPEN |
| REM-011 | Identity and Access Management | LT-IAM-005 | 30 days | OPEN |
| REM-009 | Infrastructure Engineering | LT-IAM-003 | 30 days | OPEN |
| REM-002 | Identity and Access Management | LT-IAM-002 | 30 days | OPEN |
| REM-006 | Infrastructure Engineering | LT-IAM-005 | 30 days | OPEN |
| REM-001 | Identity and Access Management | LT-IAM-002 | 60 days | OPEN |
| REM-004 | Infrastructure Engineering | LT-IAM-005 | 60 days | OPEN |
| REM-005 | Infrastructure Engineering | LT-IAM-005 | 60 days | OPEN |
| REM-003 | Infrastructure Service Owner | LT-IAM-003 | 60 days | OPEN |
| REM-010 | IT Operations Manager | LT-IAM-004 | 90 days | OPEN |

## Engineering Outcome

Task 3 operationalizes identity governance as an engineering workflow rather than a static access-review exercise. The pipeline connects identity relationships to attack-path exposure, exposure findings, residual-risk scoring, framework-mapped remediation, validation requirements, and evidence integrity.

## Evidence Chain

```text
Identity graph → Exposure findings → IAM risk register → Remediation register → Evidence manifest → Executive report
```

## Recommended Next Actions

1. Replace synthetic graph data with authorized Active Directory and BloodHound exports.
2. Integrate privileged-account and service-account checks into scheduled validation.
3. Track remediation status and post-remediation blast-radius reduction over time.
4. Feed validated IAM findings into the Domain 4 executive cyber resilience dashboard.
