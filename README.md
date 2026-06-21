# AI Management System (ISO/IEC 42001) as Code

Governing AI the way mature organizations govern security: with a **defined management system, mapped controls, automated evidence, and continuous oversight** — not a policy PDF that no one operationalizes.

This repo is a working pattern for an **AI Management System (AIMS)** built to **ISO/IEC 42001:2023**, crosswalked to the **NIST AI Risk Management Framework** and **ISO/IEC 23894** (AI risk management). It's aimed at regulated environments — **federal, healthcare, critical infrastructure** — where "we use AI responsibly" now has to be *demonstrable* to an auditor, a regulator, and a board.

> **Standards- and vendor-neutral.** Examples use published standards (ISO/IEC 42001, NIST AI RMF). All controls, mappings, and evidence are illustrative and synthetic — nothing here reflects any organization's actual AI system or implementation.

---

## Why this exists

Every organization deploying AI is now being asked the same question from three directions — customers, regulators, and their own board: *how do you know your AI is secure, accountable, and under control?* The usual answer is a values statement and a prayer.

ISO/IEC 42001 turns that into a real management system: defined roles, risk processes, lifecycle controls, and continual improvement — the same backbone ISO 27001 gives information security. This repo makes that system **executable**:

- **AI controls defined as code** — data governance, model lifecycle, human oversight, transparency, robustness.
- **Crosswalked, not duplicated** — one control mapped across ISO 42001, NIST AI RMF, and (where they intersect) ISO 27001 and 800-53.
- **Evidence built in** — each control names the artifact that proves it and the cadence it's checked.
- **Continually improvable** — changes reviewed as diffs, like any engineering change.

---

## What's here

```
ai-management-system/
├── README.md
├── aims/
│   ├── scope-and-context.md        # AIMS scope, interested parties, AI policy (42001 Cl. 4–5)
│   └── roles-raci.md               # accountability for AI risk & oversight
├── controls/
│   └── ai-controls.yaml            # source-of-truth AI control definitions (synthetic)
├── crosswalks/
│   ├── 42001_to_nist-ai-rmf.md     # ISO 42001 ↔ NIST AI RMF functions
│   ├── 42001_to_27001.md           # where AI governance meets infosec
│   └── 42001_to_23894.md           # AIMS controls ↔ AI risk-management guidance
├── risk/
│   └── ai-risk-register.md         # AI-specific risk method (impact + likelihood + model context)
└── scripts/
    └── validate_ai_controls.py     # every AI control maps to ≥1 framework + names evidence
```

## Example: one AI control, defined once

```yaml
# controls/ai-controls.yaml  (synthetic example)
- id: AIMS-OVS-1
  title: Human Oversight of AI Decisions
  statement: >
    AI systems affecting individuals provide meaningful human review of
    consequential outputs, with documented authority to override or halt.
  ai_lifecycle_stage: deployment + operation
  maps_to:
    iso_42001: [A.9.2, A.9.3]          # operation & human oversight controls
    nist_ai_rmf: [GOVERN-1.2, MANAGE-2.2]
    iso_27001: [A.5.1]                  # where governance overlaps
  evidence:
    - source: model-deployment-record
      artifact: oversight-design + override-log-sample
      cadence: per-release + quarterly-review
```

That single definition answers ISO 42001, NIST AI RMF, and the infosec overlap at once — and points at the evidence that proves it.

---

---

## Verify it yourself

```bash
# AI control catalog integrity — every control has a lifecycle stage,
# maps to >=1 framework, and names evidence
pip install pyyaml
python scripts/validate_ai_controls.py
```

This runs automatically in CI on every push and pull request (see [`.github/workflows/validate.yml`](.github/workflows/validate.yml)).

---

## Design principles

1. **A management system, not a manifesto** — AI governance is roles, risk, controls, and review, or it's nothing.
2. **Map AI controls to security controls** — AIMS doesn't replace your ISMS; it extends it. Show the seams.
3. **Lifecycle-aware** — controls attach to a stage (data → training → deployment → operation → retirement), not the abstract "the AI."
4. **Evidence is part of the control** — an AI control with no provable artifact isn't a control.
5. **Human judgment stays human** — this scaffolds and validates structure; whether a control is *adequate for the risk* is an expert call, not a script's.

## Who it's for

GRC leads, AI governance owners, and security engineers standing up AI assurance in regulated environments — and anyone who has to make "responsible AI" survive contact with an actual audit.

---

## License

MIT — see [`LICENSE`](LICENSE).

*Original work. All controls, mappings, risk entries, and evidence references are illustrative and synthetic; nothing here reflects any organization's actual AI system, model, or control implementation.*
