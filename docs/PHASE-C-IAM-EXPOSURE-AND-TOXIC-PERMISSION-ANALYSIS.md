# Phase C — IAM Exposure and Toxic-Permission Analysis

## Objective

Identify identity conditions that create elevated enterprise risk, including dormant privileged accounts, unowned service accounts, direct administrative access to high-value assets, privilege concentration, and toxic permission combinations.

## Exposure Rules

| Rule ID | Exposure Condition | Governance Risk |
|---|---|---|
| IAM-EXP-001 | Privileged account inactive for 30+ days | Dormant privileged access |
| IAM-EXP-002 | Service account has no accountable owner | Unmanaged non-human identity |
| IAM-EXP-003 | Service account has high privilege and access to a critical asset | High-impact service-account exposure |
| IAM-EXP-004 | Identity or group has direct administrative access to a critical asset | Critical administrative path |
| IAM-EXP-005 | Identity has both delegated/helpdesk capability and an active session on a managed asset | Potential privilege-abuse path |
| IAM-EXP-006 | Privileged identity can reach multiple high-value assets | Privilege concentration and elevated blast radius |

## Toxic Permission Definition

A toxic permission combination exists when separate permissions combine to create disproportionate control, escalation opportunity, or access to critical systems.

Examples include:

- Privileged group membership plus direct administrative access to a critical asset
- High-privilege service account plus remote access to a domain controller
- Delegated support permissions plus active sessions on managed endpoints
- One identity with administrative reach across multiple high-value assets

## Deliverables

- IAM exposure findings
- Toxic-permission findings
- Exposure severity distribution
- Governance observations for Phase D risk scoring
