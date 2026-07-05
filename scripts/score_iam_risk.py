#!/usr/bin/env python3
"""
Convert IAM exposure findings into a residual-risk register and
blast-radius analytics output for Lighthouse Technology Task 3.
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FINDINGS_FILE = BASE_DIR / "output" / "iam_exposure_findings.json"
GRAPH_FILE = BASE_DIR / "datasets" / "identity_privilege_graph.json"
OUTPUT_FILE = BASE_DIR / "output" / "iam_risk_register.json"


RULE_SCORES = {
    "IAM-EXP-001": {
        "likelihood": 3,
        "impact": 5,
        "control_effectiveness": 2,
        "confidence": 4,
        "description": "Dormant privileged identity retains elevated capability."
    },
    "IAM-EXP-002": {
        "likelihood": 3,
        "impact": 4,
        "control_effectiveness": 2,
        "confidence": 4,
        "description": "Service account lacks accountable ownership."
    },
    "IAM-EXP-003": {
        "likelihood": 4,
        "impact": 5,
        "control_effectiveness": 2,
        "confidence": 5,
        "description": "High-privilege service account can reach a high-value or critical asset."
    },
    "IAM-EXP-004": {
        "likelihood": 3,
        "impact": 5,
        "control_effectiveness": 3,
        "confidence": 5,
        "description": "Administrative path exists to a high-value or critical asset."
    },
    "IAM-EXP-005": {
        "likelihood": 3,
        "impact": 3,
        "control_effectiveness": 3,
        "confidence": 3,
        "description": "Delegated support access and active endpoint session create potential privilege-abuse conditions."
    },
    "IAM-EXP-006": {
        "likelihood": 4,
        "impact": 5,
        "control_effectiveness": 2,
        "confidence": 5,
        "description": "Privilege concentration expands potential blast radius across multiple high-value assets."
    }
}


def risk_rating(score):
    if score >= 16:
        return "critical"
    if score >= 10:
        return "high"
    if score >= 5:
        return "medium"
    return "low"


def asset_blast_radius(criticality):
    return {
        "critical": 4,
        "high": 2,
        "medium": 1,
        "low": 1
    }.get(criticality, 1)


def main():
    findings_data = json.loads(FINDINGS_FILE.read_text(encoding="utf-8"))
    graph_data = json.loads(GRAPH_FILE.read_text(encoding="utf-8"))

    nodes = {node["id"]: node for node in graph_data.get("nodes", [])}
    edges = graph_data.get("edges", [])

    reachable_assets = defaultdict(list)

    for edge in edges:
        target = nodes.get(edge["target"], {})
        if (
            target.get("type") == "asset"
            and edge.get("relationship") in {"ADMIN_TO", "CAN_RDP_TO"}
        ):
            reachable_assets[edge["source"]].append(target)

    name_to_id = {
        node.get("name"): node_id
        for node_id, node in nodes.items()
        if node.get("name")
    }

    risk_register = []

    for finding in findings_data.get("findings", []):
        rule_id = finding["rule_id"]
        base = RULE_SCORES[rule_id]

        subject = finding["subject"]
        subject_id = name_to_id.get(subject)
        assets = reachable_assets.get(subject_id, [])

        blast_radius = 1
        reachable_asset_names = []

        if assets:
            blast_radius = max(asset_blast_radius(asset.get("criticality")) for asset in assets)
            reachable_asset_names = sorted({asset.get("name") for asset in assets})

            if len(reachable_asset_names) >= 2:
                blast_radius = min(5, blast_radius + 1)

        evidence = finding.get("evidence", {})
        target_criticality = evidence.get("asset_criticality")
        if target_criticality:
            blast_radius = max(blast_radius, asset_blast_radius(target_criticality))

        likelihood = base["likelihood"]
        impact = base["impact"]
        control_effectiveness = base["control_effectiveness"]
        confidence = base["confidence"]

        inherent_risk = likelihood * impact
        residual_risk = inherent_risk * (1 - (control_effectiveness / 5))

        # Add a controlled blast-radius adjustment without exceeding 25.
        adjusted_residual_risk = min(25, round(residual_risk + (blast_radius - 1) * 1.5, 2))

        risk_register.append({
            "risk_id": f"RISK-{finding['finding_id'].split('-')[-1]}",
            "finding_id": finding["finding_id"],
            "rule_id": rule_id,
            "risk_title": finding["title"],
            "subject": subject,
            "risk_description": base["description"],
            "likelihood": likelihood,
            "impact": impact,
            "inherent_risk": inherent_risk,
            "control_effectiveness": control_effectiveness,
            "confidence": confidence,
            "blast_radius": blast_radius,
            "reachable_assets": reachable_asset_names,
            "residual_risk": adjusted_residual_risk,
            "risk_rating": risk_rating(adjusted_residual_risk),
            "treatment_recommendation": finding["recommendation"],
            "evidence_reference": "output/iam_exposure_findings.json"
        })

    risk_register.sort(key=lambda item: item["residual_risk"], reverse=True)

    rating_distribution = Counter(item["risk_rating"] for item in risk_register)
    blast_radius_distribution = Counter(str(item["blast_radius"]) for item in risk_register)

    priority_queue = [
        {
            "priority": index,
            "risk_id": item["risk_id"],
            "subject": item["subject"],
            "rating": item["risk_rating"],
            "residual_risk": item["residual_risk"],
            "recommended_action": item["treatment_recommendation"]
        }
        for index, item in enumerate(risk_register, start=1)
    ]

    output = {
        "project": "Lighthouse Technology - Domain 4 Task 3",
        "analysis": "Identity Risk Scoring and Blast-Radius Analytics",
        "methodology": {
            "scale": "1-5",
            "formula": "Residual Risk = (Likelihood x Impact) x (1 - Control Effectiveness/5) + Blast Radius Adjustment",
            "risk_bands": {
                "critical": "16-25",
                "high": "10-15.99",
                "medium": "5-9.99",
                "low": "1-4.99"
            }
        },
        "summary": {
            "risk_count": len(risk_register),
            "rating_distribution": dict(rating_distribution),
            "blast_radius_distribution": dict(blast_radius_distribution),
            "highest_residual_risk": risk_register[0]["residual_risk"] if risk_register else 0
        },
        "risk_register": risk_register,
        "priority_remediation_queue": priority_queue
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print("[SUCCESS] IAM risk register generated.")
    print(f"[INFO] Output: {OUTPUT_FILE}")
    print(f"[INFO] Risks scored: {len(risk_register)}")
    print(f"[INFO] Risk distribution: {dict(rating_distribution)}")
    print(f"[INFO] Highest residual risk: {output['summary']['highest_residual_risk']}")


if __name__ == "__main__":
    main()
