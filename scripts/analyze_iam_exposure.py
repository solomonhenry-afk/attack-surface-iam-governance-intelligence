#!/usr/bin/env python3
"""
Analyze the Lighthouse Technology synthetic privilege graph for IAM exposure
and toxic-permission combinations.
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "datasets" / "identity_privilege_graph.json"
OUTPUT_FILE = BASE_DIR / "output" / "iam_exposure_findings.json"


def finding(finding_id, rule_id, title, severity, subject, evidence, recommendation):
    return {
        "finding_id": finding_id,
        "rule_id": rule_id,
        "title": title,
        "severity": severity,
        "subject": subject,
        "evidence": evidence,
        "recommendation": recommendation
    }


def main():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        graph = json.load(file)

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    node_lookup = {node["id"]: node for node in nodes}
    outbound = defaultdict(list)

    for edge in edges:
        outbound[edge["source"]].append(edge)

    findings = []
    counter = 1

    # IAM-EXP-001: dormant privileged accounts
    for node in nodes:
        if node.get("type") in {"user", "service_account"}:
            privileged = node.get("privilege_tier") in {"high", "domain_admin"}
            dormant = node.get("last_logon_days", 0) >= 30

            if privileged and dormant:
                findings.append(
                    finding(
                        f"F-{counter:03d}",
                        "IAM-EXP-001",
                        "Dormant privileged identity",
                        "high",
                        node.get("name"),
                        {
                            "identity_type": node.get("type"),
                            "privilege_tier": node.get("privilege_tier"),
                            "last_logon_days": node.get("last_logon_days")
                        },
                        "Validate business need, disable or remove elevated access, and retain review evidence."
                    )
                )
                counter += 1

    # IAM-EXP-002: unowned service accounts
    for node in nodes:
        if node.get("type") == "service_account" and node.get("owner") == "Unassigned":
            findings.append(
                finding(
                    f"F-{counter:03d}",
                    "IAM-EXP-002",
                    "Service account without accountable owner",
                    "high",
                    node.get("name"),
                    {
                        "privilege_tier": node.get("privilege_tier"),
                        "last_logon_days": node.get("last_logon_days"),
                        "owner": node.get("owner")
                    },
                    "Assign a business and technical owner, validate purpose, rotate credentials, and reduce privileges."
                )
            )
            counter += 1

    # Direct paths to high-value assets
    high_value_assets = {"high", "critical"}
    high_value_paths = defaultdict(list)

    for edge in edges:
        source = node_lookup.get(edge["source"], {})
        target = node_lookup.get(edge["target"], {})

        if (
            target.get("type") == "asset"
            and target.get("criticality") in high_value_assets
            and edge.get("relationship") in {"ADMIN_TO", "CAN_RDP_TO"}
        ):
            high_value_paths[edge["source"]].append({
                "relationship": edge["relationship"],
                "asset": target.get("name"),
                "criticality": target.get("criticality"),
                "network_zone": target.get("network_zone")
            })

            severity = "critical" if target.get("criticality") == "critical" else "high"

            findings.append(
                finding(
                    f"F-{counter:03d}",
                    "IAM-EXP-003" if source.get("type") == "service_account" else "IAM-EXP-004",
                    "High-privilege service account path to critical asset"
                    if source.get("type") == "service_account"
                    else "Administrative path to high-value asset",
                    severity,
                    source.get("name"),
                    {
                        "source_type": source.get("type"),
                        "relationship": edge.get("relationship"),
                        "target_asset": target.get("name"),
                        "asset_criticality": target.get("criticality"),
                        "network_zone": target.get("network_zone")
                    },
                    "Review access necessity, enforce least privilege, apply segmentation controls, and monitor privileged activity."
                )
            )
            counter += 1

    # IAM-EXP-005: helpdesk membership plus session on a managed endpoint
    helpdesk_members = set()
    managed_endpoint_sessions = set()

    for edge in edges:
        source = node_lookup.get(edge["source"], {})
        target = node_lookup.get(edge["target"], {})

        if (
            edge.get("relationship") == "MEMBER_OF"
            and target.get("type") == "group"
            and target.get("name") == "Helpdesk"
        ):
            helpdesk_members.add(edge["source"])

        if (
            edge.get("relationship") == "HAS_SESSION_ON"
            and target.get("type") == "asset"
        ):
            managed_endpoint_sessions.add(edge["source"])

    for identity_id in helpdesk_members.intersection(managed_endpoint_sessions):
        identity = node_lookup[identity_id]
        findings.append(
            finding(
                f"F-{counter:03d}",
                "IAM-EXP-005",
                "Delegated support access combined with active managed-asset session",
                "medium",
                identity.get("name"),
                {
                    "group": "Helpdesk",
                    "condition": "Active session on managed endpoint"
                },
                "Review delegated rights, session monitoring, endpoint administrative controls, and separation-of-duties requirements."
            )
        )
        counter += 1

    # IAM-EXP-006: one source reaches multiple high-value assets
    for source_id, paths in high_value_paths.items():
        unique_assets = {path["asset"] for path in paths}

        if len(unique_assets) >= 2:
            source = node_lookup[source_id]
            findings.append(
                finding(
                    f"F-{counter:03d}",
                    "IAM-EXP-006",
                    "Privilege concentration across multiple high-value assets",
                    "high",
                    source.get("name"),
                    {
                        "source_type": source.get("type"),
                        "reachable_assets": sorted(unique_assets),
                        "path_count": len(paths)
                    },
                    "Reduce privilege concentration, separate administrative duties, and validate whether access can be scoped by system or role."
                )
            )
            counter += 1

    severity_distribution = Counter(item["severity"] for item in findings)
    rule_distribution = Counter(item["rule_id"] for item in findings)

    output = {
        "project": graph.get("project"),
        "analysis": "IAM Exposure and Toxic-Permission Analysis",
        "finding_count": len(findings),
        "severity_distribution": dict(severity_distribution),
        "rule_distribution": dict(rule_distribution),
        "findings": findings,
        "governance_summary": {
            "high_or_critical_findings": sum(
                1 for item in findings if item["severity"] in {"high", "critical"}
            ),
            "next_phase": "Phase D — Identity Risk Scoring and Blast-Radius Analytics",
            "note": "Findings are generated from a synthetic training graph and should be replaced or enriched with authorized enterprise data in a production environment."
        }
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(output, file, indent=2)

    print("[SUCCESS] IAM exposure analysis completed.")
    print(f"[INFO] Output: {OUTPUT_FILE}")
    print(f"[INFO] Findings: {len(findings)}")
    print(f"[INFO] Severity distribution: {dict(severity_distribution)}")
    print(f"[INFO] High/Critical findings: {output['governance_summary']['high_or_critical_findings']}")


if __name__ == "__main__":
    main()
