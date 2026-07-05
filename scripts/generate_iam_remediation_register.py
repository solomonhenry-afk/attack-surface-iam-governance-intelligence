#!/usr/bin/env python3
"""
Generate a governance-correlated IAM remediation register from the
Lighthouse Technology Task 3 IAM risk register.
"""

import json
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "output" / "iam_risk_register.json"
OUTPUT_FILE = BASE_DIR / "output" / "iam_governance_remediation_register.json"


CONTROL_MAPPING = {
    "IAM-EXP-001": {
        "lighthouse_control": "LT-IAM-002",
        "control_objective": "Dormant privileged accounts are identified and reviewed",
        "nist_csf": ["PR.AA"],
        "cis_controls": ["5"],
        "iso_27001": ["A.5.16", "A.5.18"],
        "owner": "Identity and Access Management",
        "evidence_required": [
            "Account review record",
            "Disablement or privilege-removal evidence",
            "Post-remediation privileged-group export"
        ],
        "validation_method": "Re-run privileged account activity review and confirm the account no longer retains unnecessary elevated access."
    },
    "IAM-EXP-002": {
        "lighthouse_control": "LT-IAM-003",
        "control_objective": "Service accounts have accountable owners and controlled privileges",
        "nist_csf": ["PR.AA"],
        "cis_controls": ["5", "6"],
        "iso_27001": ["A.5.16", "A.5.18"],
        "owner": "Infrastructure Service Owner",
        "evidence_required": [
            "Named business owner",
            "Named technical owner",
            "Service-account purpose record",
            "Credential rotation evidence"
        ],
        "validation_method": "Confirm ownership is populated, business purpose is approved, and access remains limited to documented service requirements."
    },
    "IAM-EXP-003": {
        "lighthouse_control": "LT-IAM-003",
        "control_objective": "Service accounts have accountable owners and controlled privileges",
        "nist_csf": ["PR.AA", "PR.PS"],
        "cis_controls": ["5", "6"],
        "iso_27001": ["A.5.15", "A.5.18", "A.8.2"],
        "owner": "Infrastructure Engineering",
        "evidence_required": [
            "Service-account privilege review",
            "Updated group membership export",
            "Firewall or segmentation validation",
            "Credential rotation evidence"
        ],
        "validation_method": "Verify the service account cannot perform unnecessary administrative or remote-access actions against critical systems."
    },
    "IAM-EXP-004": {
        "lighthouse_control": "LT-IAM-005",
        "control_objective": "Identity attack paths are evaluated for blast-radius risk",
        "nist_csf": ["ID.RA", "PR.AA"],
        "cis_controls": ["4", "5", "6"],
        "iso_27001": ["A.5.15", "A.5.18", "A.8.8"],
        "owner": "Infrastructure Engineering",
        "evidence_required": [
            "Privileged group membership export",
            "Asset administrative-access review",
            "Network segmentation validation",
            "Updated attack-path analysis"
        ],
        "validation_method": "Re-run the privilege graph and verify the unnecessary administrative path to the high-value asset is removed or reduced."
    },
    "IAM-EXP-005": {
        "lighthouse_control": "LT-IAM-004",
        "control_objective": "Privilege inheritance and toxic permissions are assessed",
        "nist_csf": ["PR.AA"],
        "cis_controls": ["5", "6"],
        "iso_27001": ["A.5.15", "A.5.18"],
        "owner": "IT Operations Manager",
        "evidence_required": [
            "Delegated-permission review",
            "Endpoint session review",
            "Separation-of-duties approval"
        ],
        "validation_method": "Confirm delegated support access is scoped, monitored, and separated from unnecessary administrative capability."
    },
    "IAM-EXP-006": {
        "lighthouse_control": "LT-IAM-005",
        "control_objective": "Identity attack paths are evaluated for blast-radius risk",
        "nist_csf": ["ID.RA", "PR.AA"],
        "cis_controls": ["4", "5", "6"],
        "iso_27001": ["A.5.15", "A.8.8"],
        "owner": "Identity and Access Management",
        "evidence_required": [
            "Role redesign record",
            "Updated privileged-group membership",
            "Updated attack-path analysis",
            "Post-remediation blast-radius score"
        ],
        "validation_method": "Re-run graph analysis and confirm high-value asset reachability and blast radius have decreased."
    }
}


def treatment_window(rating):
    return {
        "critical": {"days": 7, "status": "open", "escalation": "Immediate security and infrastructure escalation"},
        "high": {"days": 30, "status": "open", "escalation": "Assigned owner and weekly review"},
        "medium": {"days": 60, "status": "open", "escalation": "Monthly governance review"},
        "low": {"days": 90, "status": "open", "escalation": "Routine control-improvement backlog"}
    }[rating]


def main():
    risk_data = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    remediation_items = []

    for risk in risk_data["risk_register"]:
        mapping = CONTROL_MAPPING[risk["rule_id"]]
        treatment = treatment_window(risk["risk_rating"])

        remediation_items.append({
            "remediation_id": f"REM-{risk['risk_id'].split('-')[-1]}",
            "risk_id": risk["risk_id"],
            "finding_id": risk["finding_id"],
            "subject": risk["subject"],
            "risk_title": risk["risk_title"],
            "risk_rating": risk["risk_rating"],
            "residual_risk": risk["residual_risk"],
            "blast_radius": risk["blast_radius"],
            "lighthouse_control": mapping["lighthouse_control"],
            "control_objective": mapping["control_objective"],
            "framework_mapping": {
                "nist_csf": mapping["nist_csf"],
                "cis_controls": mapping["cis_controls"],
                "iso_27001": mapping["iso_27001"]
            },
            "remediation_owner": mapping["owner"],
            "target_treatment_days": treatment["days"],
            "workflow_status": treatment["status"],
            "escalation_requirement": treatment["escalation"],
            "remediation_action": risk["treatment_recommendation"],
            "evidence_required": mapping["evidence_required"],
            "validation_method": mapping["validation_method"],
            "source_evidence": [
                "output/iam_exposure_findings.json",
                "output/iam_risk_register.json",
                "datasets/identity_privilege_graph.json"
            ]
        })

    remediation_items.sort(key=lambda item: item["residual_risk"], reverse=True)

    control_distribution = Counter(item["lighthouse_control"] for item in remediation_items)
    owner_distribution = Counter(item["remediation_owner"] for item in remediation_items)
    rating_distribution = Counter(item["risk_rating"] for item in remediation_items)

    output = {
        "project": "Lighthouse Technology - Domain 4 Task 3",
        "analysis": "Governance Correlation and Remediation Intelligence",
        "summary": {
            "remediation_item_count": len(remediation_items),
            "risk_rating_distribution": dict(rating_distribution),
            "control_distribution": dict(control_distribution),
            "owner_distribution": dict(owner_distribution),
            "map_once_comply_many": "Each Lighthouse IAM control is mapped to NIST CSF, CIS Controls, and ISO/IEC 27001 references."
        },
        "remediation_register": remediation_items
    }

    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print("[SUCCESS] IAM governance remediation register generated.")
    print(f"[INFO] Output: {OUTPUT_FILE}")
    print(f"[INFO] Remediation items: {len(remediation_items)}")
    print(f"[INFO] Control distribution: {dict(control_distribution)}")
    print(f"[INFO] Owner distribution: {dict(owner_distribution)}")


if __name__ == "__main__":
    main()
