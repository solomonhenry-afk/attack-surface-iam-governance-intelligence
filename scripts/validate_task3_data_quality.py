#!/usr/bin/env python3
"""
Validate traceability and required governance fields for Domain 4 Task 3.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FILES = {
    "findings": BASE_DIR / "output" / "iam_exposure_findings.json",
    "risks": BASE_DIR / "output" / "iam_risk_register.json",
    "remediation": BASE_DIR / "output" / "iam_governance_remediation_register.json",
    "manifest": BASE_DIR / "evidence" / "task3_evidence_manifest.json"
}


def load_json(label):
    path = FILES[label]
    if not path.exists():
        raise FileNotFoundError(f"Required file is missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    errors = []
    findings_data = load_json("findings")
    risks_data = load_json("risks")
    remediation_data = load_json("remediation")
    manifest_data = load_json("manifest")

    findings = findings_data.get("findings", [])
    risks = risks_data.get("risk_register", [])
    remediation_items = remediation_data.get("remediation_register", [])

    finding_ids = {item.get("finding_id") for item in findings}
    risk_ids = {item.get("risk_id") for item in risks}

    for item in findings:
        if not item.get("severity"):
            errors.append(f"Finding {item.get('finding_id')} has no severity.")
        if not item.get("recommendation"):
            errors.append(f"Finding {item.get('finding_id')} has no recommendation.")

    for item in risks:
        if item.get("finding_id") not in finding_ids:
            errors.append(f"Risk {item.get('risk_id')} references an unknown finding.")
        if item.get("residual_risk") is None:
            errors.append(f"Risk {item.get('risk_id')} has no residual risk.")
        if not item.get("risk_rating"):
            errors.append(f"Risk {item.get('risk_id')} has no rating.")

    for item in remediation_items:
        if item.get("risk_id") not in risk_ids:
            errors.append(f"Remediation {item.get('remediation_id')} references an unknown risk.")

        required_fields = [
            "lighthouse_control",
            "remediation_owner",
            "remediation_action",
            "evidence_required",
            "validation_method",
            "target_treatment_days"
        ]

        for field in required_fields:
            if not item.get(field):
                errors.append(
                    f"Remediation {item.get('remediation_id')} is missing: {field}"
                )

    missing_manifest_artifacts = [
        item["path"]
        for item in manifest_data.get("artifacts", [])
        if not item.get("exists")
    ]

    if missing_manifest_artifacts:
        errors.append(
            "Evidence manifest reports missing artifacts: "
            + ", ".join(missing_manifest_artifacts)
        )

    print("\nLighthouse Technology — Task 3 Data Quality Validation")
    print("-" * 60)
    print(f"Findings checked: {len(findings)}")
    print(f"Risks checked: {len(risks)}")
    print(f"Remediation items checked: {len(remediation_items)}")
    print(f"Evidence artifacts checked: {len(manifest_data.get('artifacts', []))}")

    if errors:
        print("\n[FAILED] Validation found issues:")
        for error in errors:
            print(f" - {error}")
        raise SystemExit(1)

    print("\n[SUCCESS] All Task 3 traceability and governance checks passed.")


if __name__ == "__main__":
    main()
