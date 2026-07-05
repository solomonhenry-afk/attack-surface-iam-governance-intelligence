#!/usr/bin/env python3
"""
Generate a Markdown executive IAM governance report for Domain 4 Task 3.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RISK_FILE = BASE_DIR / "output" / "iam_risk_register.json"
REMEDIATION_FILE = BASE_DIR / "output" / "iam_governance_remediation_register.json"
OUTPUT_FILE = BASE_DIR / "reports" / "TASK-3-IAM-GOVERNANCE-EXECUTIVE-REPORT.md"


def main():
    risk_data = json.loads(RISK_FILE.read_text(encoding="utf-8"))
    remediation_data = json.loads(REMEDIATION_FILE.read_text(encoding="utf-8"))

    summary = risk_data["summary"]
    risks = risk_data["risk_register"]
    remediation_items = remediation_data["remediation_register"]

    top_risks = risks[:5]

    lines = [
        "# Executive IAM Governance Report",
        "",
        "## Lighthouse Technology",
        "### Domain 4 — Enterprise GRC Intelligence, Risk Analytics & Cyber Resilience Engineering",
        "### Task 3 — Attack-Surface & IAM Governance Intelligence",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "> **Training-data notice:** This report is generated from a synthetic identity and privilege graph. It demonstrates an evidence-driven governance workflow and does not represent live enterprise findings.",
        "",
        "## Executive Summary",
        "",
        f"- **IAM risks scored:** {summary['risk_count']}",
        f"- **Highest residual risk:** {summary['highest_residual_risk']}",
        f"- **Risk distribution:** {summary['rating_distribution']}",
        f"- **Blast-radius distribution:** {summary['blast_radius_distribution']}",
        "",
        "## Top Prioritized IAM Risks",
        "",
        "| Priority | Risk ID | Subject | Rating | Residual Risk | Blast Radius |",
        "|---:|---|---|---|---:|---:|"
    ]

    for index, risk in enumerate(top_risks, start=1):
        lines.append(
            f"| {index} | {risk['risk_id']} | {risk['subject']} | "
            f"{risk['risk_rating'].upper()} | {risk['residual_risk']} | "
            f"{risk['blast_radius']} |"
        )

    lines.extend([
        "",
        "## Governance and Remediation Coverage",
        "",
        "| Remediation ID | Owner | Lighthouse Control | Treatment Window | Status |",
        "|---|---|---|---:|---|"
    ])

    for item in remediation_items:
        lines.append(
            f"| {item['remediation_id']} | {item['remediation_owner']} | "
            f"{item['lighthouse_control']} | {item['target_treatment_days']} days | "
            f"{item['workflow_status'].upper()} |"
        )

    lines.extend([
        "",
        "## Engineering Outcome",
        "",
        "Task 3 operationalizes identity governance as an engineering workflow rather than a static access-review exercise. The pipeline connects identity relationships to attack-path exposure, exposure findings, residual-risk scoring, framework-mapped remediation, validation requirements, and evidence integrity.",
        "",
        "## Evidence Chain",
        "",
        "```text",
        "Identity graph → Exposure findings → IAM risk register → Remediation register → Evidence manifest → Executive report",
        "```",
        "",
        "## Recommended Next Actions",
        "",
        "1. Replace synthetic graph data with authorized Active Directory and BloodHound exports.",
        "2. Integrate privileged-account and service-account checks into scheduled validation.",
        "3. Track remediation status and post-remediation blast-radius reduction over time.",
        "4. Feed validated IAM findings into the Domain 4 executive cyber resilience dashboard.",
        ""
    ])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("[SUCCESS] Executive IAM governance report generated.")
    print(f"[INFO] Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
