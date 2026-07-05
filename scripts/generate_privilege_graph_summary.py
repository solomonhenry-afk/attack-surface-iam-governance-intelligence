#!/usr/bin/env python3
"""
Generate a governance-focused summary from the Lighthouse Technology
synthetic identity privilege graph.
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "datasets" / "identity_privilege_graph.json"
OUTPUT_FILE = BASE_DIR / "output" / "privilege_graph_summary.json"


def main():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        graph = json.load(file)

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    node_lookup = {node["id"]: node for node in nodes}
    node_types = Counter(node["type"] for node in nodes)
    relationship_types = Counter(edge["relationship"] for edge in edges)

    outbound = defaultdict(list)
    inbound = defaultdict(list)

    for edge in edges:
        outbound[edge["source"]].append(edge)
        inbound[edge["target"]].append(edge)

    privileged_identities = []
    dormant_privileged_identities = []
    unassigned_service_accounts = []
    critical_asset_paths = []

    for node in nodes:
        node_type = node.get("type")

        if node_type in {"user", "service_account"}:
            privilege_tier = node.get("privilege_tier", "standard")
            if privilege_tier in {"high", "domain_admin"}:
                privileged_identities.append({
                    "id": node["id"],
                    "name": node["name"],
                    "type": node_type,
                    "privilege_tier": privilege_tier,
                    "last_logon_days": node.get("last_logon_days"),
                    "owner": node.get("owner", node.get("department", "Unknown"))
                })

                if node.get("last_logon_days", 0) >= 30:
                    dormant_privileged_identities.append({
                        "id": node["id"],
                        "name": node["name"],
                        "privilege_tier": privilege_tier,
                        "last_logon_days": node["last_logon_days"]
                    })

            if node_type == "service_account" and node.get("owner") == "Unassigned":
                unassigned_service_accounts.append({
                    "id": node["id"],
                    "name": node["name"],
                    "privilege_tier": node.get("privilege_tier"),
                    "last_logon_days": node.get("last_logon_days")
                })

    for edge in edges:
        target = node_lookup.get(edge["target"], {})
        source = node_lookup.get(edge["source"], {})

        if (
            target.get("type") == "asset"
            and target.get("criticality") in {"high", "critical"}
            and edge["relationship"] in {"ADMIN_TO", "CAN_RDP_TO"}
        ):
            critical_asset_paths.append({
                "identity_or_group": source.get("name"),
                "source_type": source.get("type"),
                "relationship": edge["relationship"],
                "target_asset": target.get("name"),
                "asset_criticality": target.get("criticality"),
                "network_zone": target.get("network_zone")
            })

    summary = {
        "project": graph.get("project"),
        "graph_version": graph.get("graph_version"),
        "summary": {
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "node_types": dict(node_types),
            "relationship_types": dict(relationship_types),
            "privileged_identity_count": len(privileged_identities),
            "dormant_privileged_identity_count": len(dormant_privileged_identities),
            "unassigned_service_account_count": len(unassigned_service_accounts),
            "critical_asset_path_count": len(critical_asset_paths)
        },
        "privileged_identities": privileged_identities,
        "dormant_privileged_identities": dormant_privileged_identities,
        "unassigned_service_accounts": unassigned_service_accounts,
        "critical_asset_paths": critical_asset_paths,
        "governance_observations": [
            "Privileged identities require periodic ownership and activity review.",
            "Dormant privileged accounts require remediation priority because they retain elevated capability without recent use.",
            "Unassigned service accounts create accountability and lifecycle-governance risk.",
            "Administrative and remote-access paths to high-value assets require blast-radius analysis."
        ]
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    print("[SUCCESS] Privilege graph summary generated.")
    print(f"[INFO] Output: {OUTPUT_FILE}")
    print(f"[INFO] Nodes: {len(nodes)} | Edges: {len(edges)}")
    print(f"[INFO] Privileged identities: {len(privileged_identities)}")
    print(f"[INFO] Dormant privileged identities: {len(dormant_privileged_identities)}")
    print(f"[INFO] Critical asset paths: {len(critical_asset_paths)}")


if __name__ == "__main__":
    main()
