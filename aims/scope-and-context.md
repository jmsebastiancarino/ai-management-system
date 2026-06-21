# AIMS Scope, Context, and AI Policy

*Synthetic example satisfying ISO/IEC 42001 Clauses 4 (Context) and 5 (Leadership). Illustrative only — no real organization is represented.*

## 1. Scope of the AI Management System (Clause 4.3)

This AIMS covers all AI systems developed, deployed, or operated by the organization that make or materially support decisions affecting individuals, customers, or critical business functions. In scope: internally developed models, fine-tuned third-party models, and material use of external AI services. Out of scope: general-purpose productivity tools with no consequential decision role (reviewed annually to confirm they remain out of scope).

## 2. Context and Interested Parties (Clauses 4.1–4.2)

| Interested party | Relevant needs & expectations |
|------------------|-------------------------------|
| Affected individuals / customers | Fairness, transparency, recourse, privacy |
| Regulators | Compliance with applicable AI, sector, and data-protection law |
| Enterprise customers | Demonstrable AI assurance for due diligence |
| Leadership / board | Risk visibility, accountability, reputational protection |
| Engineering / data science | Clear, workable controls that don't block delivery |

External issues tracked: evolving AI regulation, sector-specific obligations (e.g. health, public sector), and the threat landscape for AI systems. Internal issues tracked: model inventory completeness, data governance maturity, and skills.

## 3. AI Policy (Clause 5.2)

The organization commits to:

1. **Lawful, ethical, accountable AI** — every in-scope AI system has a named accountable owner.
2. **Risk-based governance** — controls scale to the impact of the system on individuals and the business.
3. **Human oversight** — consequential AI decisions remain subject to meaningful human review and override.
4. **Transparency** — the purpose, limitations, and intended use of each AI system are documented.
5. **Data integrity** — training and operational data is lawfully sourced, quality-assessed, and provenance-tracked.
6. **Continual improvement** — incidents and monitoring feed corrective action back into the AIMS.

Policy owner: [AI Governance Lead]. Approved by: [Leadership]. Review cadence: annual or on significant regulatory/operational change.

## 4. Leadership and Roles (Clause 5.3)

Accountability sits with leadership; operational ownership is assigned per the [RACI](roles-raci.md). No AI system enters production without an assigned owner, a completed risk/impact assessment ([AIMS-RISK-1](../controls/ai-controls.yaml)), and documented human-oversight design ([AIMS-OVS-1](../controls/ai-controls.yaml)).
