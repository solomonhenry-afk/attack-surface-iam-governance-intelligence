#  Lighthouse Technology

## Attack-Surface & IAM Governance Intelligence

### Domain 4 — Enterprise GRC Intelligence, Risk Analytics & Cyber Resilience Engineering

#### Task 3 — Identity Attack-Path Analytics, Privilege Exposure & Governance Remediation

<p align="center">
  <img src="https://img.shields.io/badge/Focus-IAM%20Governance%20Intelligence-0A66C2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Analysis-Attack--Surface%20%26%20Privilege%20Risk-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-NIST%20CSF%20%7C%20CIS%20%7C%20ISO%2027001-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

#  Executive Summary

Enterprise risk does not begin only at the firewall, endpoint, or SIEM.

It often begins with an identity that has more access than it needs, a service account without accountable ownership, a dormant administrator account, a nested group relationship, or a privilege path that silently reaches a high-value asset.

This project operationalizes **Attack-Surface & IAM Governance Intelligence** for Lighthouse Technology by transforming identity relationships into measurable governance risk.

Instead of treating IAM as a periodic access-review spreadsheet, this task models:

* identities
* privileged groups
* service accounts
* administrative relationships
* high-value assets
* privilege inheritance
* attack paths
* toxic permission combinations
* blast-radius exposure
* remediation ownership
* evidence and validation requirements

The output is a governance-grade pipeline that connects technical IAM exposure to risk scoring, control correlation, remediation intelligence, evidence integrity, and executive reporting.

```text
Identity Inventory
      ↓
Privilege & Relationship Graph
      ↓
Attack-Path Analysis
      ↓
IAM Exposure Findings
      ↓
Residual-Risk & Blast-Radius Scoring
      ↓
Control / Framework Correlation
      ↓
Owner-Assigned Remediation
      ↓
Evidence Integrity Validation
      ↓
Executive IAM Governance Reporting
```

---

#  Strategic Objective

Transform Lighthouse Technology from:

```text
Periodic IAM access reviews
```

Into:

```text
Continuous identity attack-surface intelligence
```

Powered by:

```text
Privilege graph modeling
Attack-path analysis
Dormant privileged-account detection
Service-account governance
Toxic-permission analysis
Blast-radius scoring
Residual-risk analytics
Map-once, comply-many control correlation
Evidence-backed remediation validation
Executive IAM governance reporting
```

---

#  The Problem This Project Solves

Traditional IAM governance often asks:

* Who has access?
* Is the account active?
* Is the group membership approved?
* Has the access review been completed?

Those questions are necessary, but they do not explain the full enterprise risk.

This project asks the questions that matter during an attack, audit, remediation program, or executive risk review:

* Which identities can reach high-value assets?
* Which accounts retain privileged access without recent activity?
* Which service accounts lack accountable ownership?
* Which group relationships create unnecessary administrative paths?
* Which permissions create toxic combinations?
* How far could an attacker move if one identity is compromised?
* Which remediation action reduces the greatest residual risk?
* Which control, evidence, owner, and validation method prove the risk was reduced?

---

#  Task 3 Engineering Architecture

```text
┌──────────────────────────────────────────────────────────────────────┐
│                    LIGHTHOUSE TECHNOLOGY IAM DATA                    │
│                                                                      │
│  Identities • Groups • Service Accounts • Assets • Privileges        │
│  Administrative Relationships • Ownership • Criticality Tags         │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│              PRIVILEGE GRAPH & ATTACK-SURFACE MODELING               │
│                                                                      │
│  Identity → Group → Privilege → Asset → Administrative Path          │
│  Privilege Inheritance • High-Value Asset Reachability               │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│                IAM EXPOSURE & TOXIC-PERMISSION ANALYSIS              │
│                                                                      │
│  Dormant Admins • Unowned Service Accounts • Excessive Privilege     │
│  Nested Group Exposure • Toxic Permissions • Attack Paths            │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│              IDENTITY RISK & BLAST-RADIUS INTELLIGENCE               │
│                                                                      │
│  Likelihood • Impact • Control Effectiveness • Confidence            │
│  Residual Risk • Asset Criticality • Blast Radius                    │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│              GOVERNANCE CORRELATION & REMEDIATION ENGINE             │
│                                                                      │
│  Lighthouse Controls • NIST CSF • CIS Controls • ISO/IEC 27001       │
│  Owners • Treatment Windows • Evidence • Validation Methods          │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│               EVIDENCE INTEGRITY & EXECUTIVE REPORTING               │
│                                                                      │
│  SHA-256 Manifest • Data Quality Validation • Executive Report       │
│  Portfolio Evidence • Screenshot Validation                          │
└──────────────────────────────────────────────────────────────────────┘
```

---

#  Task 3 Phases

| Phase       | Capability Delivered                                   | Governance Value                                                                   |
| ----------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| **Phase A** | IAM data inventory and governance scope                | Defined identity, privilege, asset, ownership, and control scope                   |
| **Phase B** | Attack-path and privilege graph modeling               | Modeled identity-to-asset relationships and administrative reachability            |
| **Phase C** | IAM exposure and toxic-permission analysis             | Identified dormant privilege, ownership gaps, toxic combinations, and risky paths  |
| **Phase D** | Identity risk scoring and blast-radius analytics       | Prioritized exposure using residual-risk and potential impact spread               |
| **Phase E** | Governance correlation and remediation intelligence    | Assigned controls, frameworks, owners, treatment windows, evidence, and validation |
| **Phase F** | Evidence integrity, reporting, and portfolio packaging | Validated traceability and produced executive-ready reporting                      |

---

#  Phase A — IAM Data Inventory & Governance Scope

Phase A established the data model required to analyze IAM exposure as enterprise risk.

The scope included:

```text
Users
Privileged Accounts
Service Accounts
Security Groups
Administrative Groups
High-Value Assets
Privilege Relationships
Ownership Attributes
Asset Criticality
Control Requirements
```

The goal was to ensure that every later finding could be traced to a defined identity relationship and governance requirement.

---

#  Phase B — Attack-Path & Privilege Graph Modeling

Phase B modeled the identity attack surface as a relationship graph.

```text
Identity
   ↓
Security Group
   ↓
Administrative Privilege
   ↓
Critical Asset
```

This made it possible to identify paths that are difficult to see in a normal access-review spreadsheet.

Examples include:

* a user inheriting administrative access through nested group membership
* a service account retaining privilege across critical systems
* a dormant account still linked to privileged groups
* an identity path that reaches a high-value asset through multiple relationships
* a support role with excessive administrative reach

The graph model provides the technical foundation for attack-path analysis and blast-radius scoring.

---

#  Phase C — IAM Exposure & Toxic-Permission Analysis

Phase C transformed graph relationships into governance findings.

The analysis evaluated:

| Exposure Category                  | Governance Risk                                                        |
| ---------------------------------- | ---------------------------------------------------------------------- |
| Dormant privileged accounts        | Unused elevated access may be abused without timely detection          |
| Unowned service accounts           | No accountable owner for access, purpose, rotation, or review          |
| Excessive administrative privilege | Identities can perform actions beyond business necessity               |
| Nested group inheritance           | Privilege is inherited indirectly and may escape normal review         |
| Toxic permission combinations      | Combined permissions create excessive control or escalation capability |
| High-value asset reachability      | Identity compromise could provide access to critical systems           |
| Weak separation of duties          | One identity can hold conflicting or overly broad capabilities         |

Each finding includes severity, supporting evidence, and a recommended remediation action.

---

#  Phase D — Identity Risk Scoring & Blast-Radius Analytics

Phase D converts IAM exposure into prioritized business risk.

Each finding is evaluated using five dimensions:

| Risk Dimension            | Description                                                                    |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Likelihood**            | Probability that the exposure could be abused or lead to control failure       |
| **Impact**                | Potential business and security consequence                                    |
| **Control Effectiveness** | Strength of existing preventive, detective, and corrective controls            |
| **Confidence**            | Reliability of the supporting evidence                                         |
| **Blast Radius**          | Number and criticality of identities, systems, and assets potentially affected |

```text
Inherent Risk = Likelihood × Impact

Residual Risk = Inherent Risk × (1 - Control Effectiveness / 5)
                + Blast Radius Adjustment
```

| Residual Risk | Rating   | Treatment Expectation               |
| ------------: | -------- | ----------------------------------- |
|         16–25 | Critical | Immediate escalation and treatment  |
|      10–15.99 | High     | Assigned owner and weekly review    |
|        5–9.99 | Medium   | Monthly governance review           |
|        1–4.99 | Low      | Routine control-improvement backlog |

Blast-radius analytics ensure that prioritization is not based only on one vulnerable account. It also considers how many critical systems, privileges, or downstream relationships could be affected.

---

#  Phase E — Governance Correlation & Remediation Intelligence

Phase E turns technical IAM findings into accountable governance work.

```text
IAM Finding
      ↓
Residual-Risk Score
      ↓
Lighthouse Control Mapping
      ↓
Framework Correlation
      ↓
Owner Assignment
      ↓
Remediation Action
      ↓
Evidence Requirement
      ↓
Validation Method
      ↓
Residual-Risk Review
```

## Lighthouse Control Correlation

| Lighthouse Control | Control Objective                                                  | NIST CSF | CIS Controls | ISO/IEC 27001  |
| ------------------ | ------------------------------------------------------------------ | -------- | ------------ | -------------- |
| `LT-IAM-001`       | Privileged access is inventoried and monitored                     | PR.AA    | 5, 6         | A.5.15, A.5.18 |
| `LT-IAM-002`       | Dormant privileged accounts are identified and reviewed            | PR.AA    | 5            | A.5.16, A.5.18 |
| `LT-IAM-003`       | Service accounts have accountable owners and controlled privileges | PR.AA    | 5, 6         | A.5.16, A.5.18 |
| `LT-IAM-004`       | Privilege inheritance and toxic permissions are assessed           | PR.AA    | 5, 6         | A.5.15, A.5.18 |
| `LT-IAM-005`       | Identity attack paths are evaluated for blast-radius risk          | ID.RA    | 4, 5         | A.5.7, A.8.8   |
| `LT-IAM-006`       | IAM findings are mapped to remediation actions and reporting       | GV.RM    | 17           | A.5.35, A.5.36 |

## Remediation Treatment Windows

| Risk Rating | Target Window | Escalation Requirement                           |
| ----------- | ------------: | ------------------------------------------------ |
| Critical    |        7 days | Immediate security and infrastructure escalation |
| High        |       30 days | Assigned owner and weekly review                 |
| Medium      |       60 days | Monthly governance review                        |
| Low         |       90 days | Routine control-improvement backlog              |

This implements a **map-once, comply-many** model: one operational finding is correlated across multiple frameworks without rebuilding separate manual compliance narratives.

---

#  Phase F — Evidence Integrity, Reporting & Portfolio Packaging

Phase F closes the loop between analysis and governance assurance.

The evidence chain is:

```text
Identity Privilege Graph
      ↓
IAM Exposure Findings
      ↓
IAM Risk Register
      ↓
Governance Remediation Register
      ↓
SHA-256 Evidence Manifest
      ↓
Data-Quality Validation
      ↓
Executive IAM Governance Report
```

The validation process confirms that:

* required Task 3 artifacts exist
* JSON outputs are valid
* findings include severity and recommendations
* risks reference valid findings
* risks include residual-risk scores and ratings
* remediation items reference valid risks
* remediation items include controls, owners, evidence, timelines, and validation methods
* evidence artifacts are integrity-tracked with SHA-256 hashes

---

#  Repository Structure

```text
Task-3-Attack-Surface-IAM-Governance-Intelligence/
├── datasets/
│   ├── iam_governance_inventory.json
│   └── identity_privilege_graph.json
├── docs/
│   ├── PHASE-A-IAM-DATA-INVENTORY-AND-GOVERNANCE-SCOPE.md
│   ├── PHASE-B-ATTACK-PATH-AND-PRIVILEGE-GRAPH-MODELING.md
│   ├── PHASE-C-IAM-EXPOSURE-AND-TOXIC-PERMISSION-ANALYSIS.md
│   ├── PHASE-D-IDENTITY-RISK-SCORING-AND-BLAST-RADIUS-ANALYTICS.md
│   ├── PHASE-E-GOVERNANCE-CORRELATION-AND-REMEDIATION-INTELLIGENCE.md
│   ├── PHASE-F-EVIDENCE-INTEGRITY-REPORTING-AND-PORTFOLIO-PACKAGING.md
│   └── TASK-3-COMPLETION.md
├── evidence/
│   └── task3_evidence_manifest.json
├── output/
│   ├── privilege_graph_summary.json
│   ├── iam_exposure_findings.json
│   ├── iam_risk_register.json
│   └── iam_governance_remediation_register.json
├── reports/
│   └── TASK-3-IAM-GOVERNANCE-EXECUTIVE-REPORT.md
├── screenshots/
│   ├── 01-task3-pipeline-success.png
│   ├── 02-privilege-graph-summary.png
│   ├── 03-iam-exposure-findings.png
│   ├── 04-iam-risk-register.png
│   ├── 05-governance-remediation-register.png
│   ├── 06-evidence-manifest.png
│   ├── 07-data-quality-validation.png
│   ├── 08-executive-iam-report.png
│   └── 09-task3-repository-structure.png
├── scripts/
│   ├── generate_privilege_graph_summary.py
│   ├── analyze_iam_exposure.py
│   ├── score_iam_risk.py
│   ├── generate_iam_remediation_register.py
│   ├── generate_evidence_manifest.py
│   ├── validate_task3_data_quality.py
│   ├── generate_task3_executive_report.py
│   └── run_task3_pipeline.sh
└── README.md
```

---

#  Running the Full Pipeline

```bash
python3 scripts/generate_privilege_graph_summary.py
python3 scripts/analyze_iam_exposure.py
python3 scripts/score_iam_risk.py
python3 scripts/generate_iam_remediation_register.py
python3 scripts/generate_evidence_manifest.py
python3 scripts/validate_task3_data_quality.py
python3 scripts/generate_task3_executive_report.py
```

Or to run the complete workflow:

```bash
chmod +x scripts/run_task3_pipeline.sh
./scripts/run_task3_pipeline.sh
```

---

# Primary Deliverables

| Output                                              | Purpose                                                                                       |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `output/privilege_graph_summary.json`               | Summarizes identities, privileged groups, high-value assets, and administrative paths         |
| `output/iam_exposure_findings.json`                 | Records IAM exposure, toxic-permission conditions, evidence, and recommendations              |
| `output/iam_risk_register.json`                     | Scores likelihood, impact, control effectiveness, confidence, blast radius, and residual risk |
| `output/iam_governance_remediation_register.json`   | Maps risks to controls, frameworks, owners, treatment windows, evidence, and validation       |
| `evidence/task3_evidence_manifest.json`             | Produces SHA-256 integrity references for project artifacts                                   |
| `reports/TASK-3-IAM-GOVERNANCE-EXECUTIVE-REPORT.md` | Produces executive-level IAM risk and remediation reporting                                   |

---

#  Evidence Screenshots

| Screenshot                               | Evidence Demonstrated                                            |
| ---------------------------------------- | ---------------------------------------------------------------- |
| `01-task3-pipeline-success.png`          | Successful end-to-end Task 3 pipeline execution                  |
| `02-privilege-graph-summary.png`         | Identity, group, asset, and administrative-path graph output     |
| `03-iam-exposure-findings.png`           | IAM exposure and toxic-permission findings                       |
| `04-iam-risk-register.png`               | Residual-risk prioritization and blast-radius analytics          |
| `05-governance-remediation-register.png` | Framework-mapped remediation ownership, evidence, and validation |
| `06-evidence-manifest.png`               | SHA-256 evidence manifest generation                             |
| `07-data-quality-validation.png`         | Successful traceability and governance-field validation          |
| `08-executive-iam-report.png`            | Executive IAM governance report                                  |
| `09-task3-repository-structure.png`      | Final project structure                                          |

---

#  Lighthouse Technology Security Evolution Analytics

| Domain                | Security Engineering Focus                         | Core Outcome                                                                                             |
| --------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Domain 1**          | Enterprise Security Architecture & Threat Modeling | Security architecture, attack-surface understanding, and enterprise control design                       |
| **Domain 2**          | Detection Engineering & Security Operations        | Telemetry, SIEM analytics, detection logic, incident investigation, and response workflows               |
| **Domain 3**          | Network Security & Infrastructure Engineering      | VLAN segmentation, firewall governance, IDS/IPS, east-west traffic analysis, and remediation engineering |
| **Domain 4 — Task 1** | Enterprise Risk Telemetry Engineering              | Governance-grade telemetry ingestion, normalization, enrichment, and evidence generation                 |
| **Domain 4 — Task 2** | Automated GRC Control Validation Engine            | Continuous control testing, drift detection, remediation correlation, and governance reporting           |
| **Domain 4 — Task 3** | Attack-Surface & IAM Governance Intelligence       | Privilege graph analysis, identity risk scoring, blast-radius analytics, and evidence-backed remediation |

```text
Security Architecture
        +
Detection Engineering
        +
Network Security Engineering
        +
Telemetry-Driven GRC
        +
Automated Control Validation
        +
IAM Attack-Surface Intelligence
        =
Enterprise Cyber Resilience Engineering
```

---

#  Tech Stack

| Category                     | Technologies / Methods                                                                                                                   |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Programming & Automation** | Python 3, JSON, Bash                                                                                                                     |
| **IAM Analytics**            | Identity inventory modeling, privilege graph analysis, attack-path correlation, toxic-permission analysis                                |
| **Risk Engineering**         | Likelihood scoring, impact scoring, control-effectiveness scoring, confidence scoring, blast-radius analytics, residual-risk calculation |
| **Governance & Compliance**  | NIST CSF, CIS Controls, ISO/IEC 27001, map-once comply-many control correlation                                                          |
| **Evidence Engineering**     | SHA-256 evidence manifests, artifact traceability, data-quality validation, validation-method tracking                                   |
| **Reporting**                | Markdown executive reports, remediation registers, risk registers, screenshot evidence                                                   |
| **Version Control**          | Git, GitHub                                                                                                                              |

---

#  GitHub Analytics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=solomonhenry-afk&show_icons=true&theme=tokyonight&hide_border=true" alt="Solomon Henry GitHub Statistics" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=solomonhenry-afk&theme=tokyonight&hide_border=true" alt="Solomon Henry GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=solomonhenry-afk&layout=compact&theme=tokyonight&hide_border=true" alt="Most Used Languages" />
</p>

---

#  Repository Visitors

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=solomonhenry-afk&label=Repository%20Visitors&color=0A66C2&style=for-the-badge" alt="Repository Visitors" />
</p>

---

# 🤝 Connect With Me

<p align="center">
  <a href="https://www.linkedin.com/in/solomon-henry/">
    <img src="https://img.shields.io/badge/LinkedIn-Solomon%20Henry-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/solomonhenry-afk">
    <img src="https://img.shields.io/badge/GitHub-solomonhenry--afk-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---

##  Enterprise Security Evolution

This repository is one component of the **Lighthouse Technology Enterprise Security Evolution** portfolio: a progressive body of work that connects security architecture, detection engineering, network infrastructure hardening, governance automation, identity risk analytics, and cyber resilience reporting.

```text
Domain 1 — Enterprise Security Architecture & Threat Modeling
        ↓
Domain 2 — Detection Engineering & Security Operations
        ↓
Domain 3 — Network Security & Infrastructure Engineering
        ↓
Domain 4 — Enterprise GRC Intelligence, Risk Analytics & Cyber Resilience Engineering
        ↓
Task 3 — Attack-Surface & IAM Governance Intelligence
```

The purpose is to demonstrate practical readiness for security engineering and modern GRC roles where technical controls, risk decisions, evidence, automation, and remediation must operate as one system.

---

#  Author

**Bassey Solomon Henry**
Cybersecurity | Detection Engineering | Network Security | GRC Engineering | IAM Governance Intelligence

I build security programs that connect technical telemetry, infrastructure controls, identity exposure, risk analytics, remediation engineering, and executive reporting.

My work focuses on transforming security from isolated tools and manual compliance processes into measurable, evidence-driven enterprise resilience.

---

#  Personal Philosophy

> **Security governance becomes credible when it is connected to operational evidence, measurable risk reduction, and accountable remediation—not when it exists only as a policy or spreadsheet.**

**— Solomon Henry**

---

# Data Notice

All datasets in this repository are synthetic and used solely for authorized cybersecurity engineering, GRC automation, IAM governance analytics, and portfolio demonstration.

This repository does not contain live enterprise identity data, credentials, confidential infrastructure details, or production access information.

---

#  Lighthouse Technology Portfolio

<p align="center">

**Lighthouse Technology — Enterprise Security Evolution**

Domain 4: **Enterprise GRC Intelligence, Risk Analytics & Cyber Resilience Engineering**
Task 3: **Attack-Surface & IAM Governance Intelligence**

Built to demonstrate that modern GRC practitioners must understand infrastructure, identity, telemetry, risk analytics, automation, evidence integrity, and remediation engineering.

**© 2026 Solomon Henry | Cybersecurity & GRC Engineering Portfolio**

</p>


---
