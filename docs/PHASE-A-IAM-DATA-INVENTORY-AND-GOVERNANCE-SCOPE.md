# Phase A — IAM Data Inventory and Governance Scope

## Objective

Define the identity, privilege, authentication, asset, and control-evidence data required to measure identity attack-surface exposure and support governance decisions.

## Governance Questions

This task is designed to answer:

- Which identities hold privileged access?
- Which accounts are dormant but retain administrative capability?
- Which service accounts create elevated exposure?
- Which privilege relationships can create lateral-movement paths?
- Which identity exposures have the largest potential blast radius?
- Which controls and remediation actions reduce residual IAM risk?

## Data Domains

| Data Domain | Purpose |
|---|---|
| User accounts | Account state, ownership, role, privilege level, and activity |
| Privileged groups | Administrative capability and delegated access |
| Service accounts | Non-human identity exposure and ownership accountability |
| Authentication telemetry | Failed logons, privileged logons, and stale-account indicators |
| Asset inventory | Criticality and business impact of reachable systems |
| Permission relationships | Direct membership, inherited access, delegation, and administrative paths |
| Existing evidence | Domain 1–4 artifacts supporting governance traceability |

## Initial Control Scope

| Control ID | Control Objective |
|---|---|
| LT-IAM-001 | Privileged access is inventoried and monitored |
| LT-IAM-002 | Dormant privileged accounts are identified and reviewed |
| LT-IAM-003 | Service accounts have accountable owners and controlled privileges |
| LT-IAM-004 | Privilege inheritance and toxic permission combinations are assessed |
| LT-IAM-005 | Identity attack paths are evaluated for blast-radius risk |
| LT-IAM-006 | IAM findings are mapped to remediation actions and governance reporting |

## Deliverables

- IAM governance data inventory
- Initial identity and asset datasets
- Control scope and evidence requirements
- Phase A documentation
