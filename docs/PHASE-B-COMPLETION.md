# Phase B Completion — Attack-Path and Privilege Graph Modeling

## Status

Completed.

## Deliverables Produced

- `datasets/identity_privilege_graph.json`
- `scripts/generate_privilege_graph_summary.py`
- `output/privilege_graph_summary.json`

## Key Findings Identified by the Initial Model

- Privileged user and service identities were identified.
- Dormant privileged-account exposure was detected.
- An unassigned service account was identified as an accountability risk.
- Administrative and remote-access relationships to high-value assets were identified.
- The resulting graph summary provides the input for Phase C exposure analysis and Phase D IAM risk scoring.

## Evidence

- Terminal output from `python3 scripts/generate_privilege_graph_summary.py`
- Formatted graph summary output
