#!/usr/bin/env python3
"""
Generate a traceability manifest for Lighthouse Technology Domain 4 Task 3.
"""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "evidence" / "task3_evidence_manifest.json"

ARTIFACTS = [
    {
        "artifact_id": "EVID-T3-001",
        "path": "datasets/iam_governance_inventory.json",
        "purpose": "Defines the IAM governance data domains and control scope."
    },
    {
        "artifact_id": "EVID-T3-002",
        "path": "datasets/identity_privilege_graph.json",
        "purpose": "Provides the synthetic identity, group, asset, and relationship graph."
    },
    {
        "artifact_id": "EVID-T3-003",
        "path": "output/privilege_graph_summary.json",
        "purpose": "Summarizes privileged identities, dormant accounts, service-account ownership gaps, and critical paths."
    },
    {
        "artifact_id": "EVID-T3-004",
        "path": "output/iam_exposure_findings.json",
        "purpose": "Records IAM exposure and toxic-permission findings."
    },
    {
        "artifact_id": "EVID-T3-005",
        "path": "output/iam_risk_register.json",
        "purpose": "Records likelihood, impact, control effectiveness, confidence, blast radius, and residual risk."
    },
    {
        "artifact_id": "EVID-T3-006",
        "path": "output/iam_governance_remediation_register.json",
        "purpose": "Maps risks to controls, frameworks, owners, remediation actions, evidence, and validation."
    }
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    manifest_items = []

    for artifact in ARTIFACTS:
        artifact_path = BASE_DIR / artifact["path"]

        manifest_items.append({
            "artifact_id": artifact["artifact_id"],
            "path": artifact["path"],
            "purpose": artifact["purpose"],
            "exists": artifact_path.exists(),
            "sha256": sha256_file(artifact_path) if artifact_path.exists() else None,
            "size_bytes": artifact_path.stat().st_size if artifact_path.exists() else None
        })

    output = {
        "project": "Lighthouse Technology - Domain 4 Task 3",
        "task": "Attack-Surface & IAM Governance Intelligence",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "integrity_method": "SHA-256",
        "synthetic_data_notice": (
            "This project uses synthetic training data. It demonstrates an "
            "evidence-driven IAM governance workflow and does not represent "
            "live enterprise findings."
        ),
        "artifact_count": len(manifest_items),
        "artifacts": manifest_items
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")

    present = sum(1 for item in manifest_items if item["exists"])
    print("[SUCCESS] Task 3 evidence manifest generated.")
    print(f"[INFO] Output: {OUTPUT_FILE}")
    print(f"[INFO] Artifacts present: {present}/{len(manifest_items)}")


if __name__ == "__main__":
    main()
