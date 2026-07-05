# Phase C Completion — IAM Exposure and Toxic-Permission Analysis

## Status

Completed.

## Deliverables Produced

- `docs/PHASE-C-IAM-EXPOSURE-AND-TOXIC-PERMISSION-ANALYSIS.md`
- `scripts/analyze_iam_exposure.py`
- `output/iam_exposure_findings.json`

## Exposure Conditions Evaluated

- Dormant privileged identities
- Unowned service accounts
- High-privilege service-account paths
- Administrative paths to high-value assets
- Delegated support access combined with active endpoint sessions
- Privilege concentration across multiple high-value assets

## Governance Outcome

The resulting findings provide structured input for residual-risk scoring and blast-radius analysis in Phase D.

## Evidence

- Successful terminal execution of `python3 scripts/analyze_iam_exposure.py`
- Formatted review of `output/iam_exposure_findings.json`
