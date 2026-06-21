# AI Risk Register (synthetic)

*Illustrative AI-specific risk method and entries. No real system or risk is represented.*

## Method

AI risk is scored on **impact** (severity of harm to individuals or the business) × **likelihood**, with an added **AI context** note capturing what makes the risk AI-specific (e.g. drift, opacity, training-data dependence) — the dimension a generic risk register misses. Scoring: Low / Medium / High / Critical. Treatment follows ISO/IEC 23894 guidance and links to the controls that address it.

| ID | Risk | AI context | Impact | Likelihood | Score | Treatment (control) |
|----|------|-----------|:------:|:----------:|:-----:|---------------------|
| R-01 | Biased outputs disadvantage a protected group | Training data not representative; bias not measured pre-deployment | High | Medium | **High** | AIMS-DATA-1, AIMS-VAL-1 |
| R-02 | Model performance degrades silently in production | Concept drift; no monitoring threshold to trigger review | High | Medium | **High** | AIMS-MON-1 |
| R-03 | Consequential decision made with no human recourse | Oversight not designed into the workflow | High | Low | **Medium** | AIMS-OVS-1 |
| R-04 | Training data unlawfully sourced or used | Provenance not recorded; lawful basis unverified | Critical | Low | **High** | AIMS-DATA-1, AIMS-GOV-1 |
| R-05 | Model or its data compromised by an attacker | AI system is also an information asset; credential/model exposure | High | Medium | **High** | AIMS-INC-1 + ISMS controls |
| R-06 | Users over-trust an opaque system | No documentation of limitations / intended use | Medium | Medium | **Medium** | AIMS-TRANS-1 |

## How this connects to the rest of the AIMS

Each register entry links to one or more controls in [`ai-controls.yaml`](../controls/ai-controls.yaml), and every in-scope AI system carries its own assessment under [AIMS-RISK-1](../controls/ai-controls.yaml). Treatment effectiveness is reviewed on the monitoring cadence (AIMS-MON-1) and after any AI incident (AIMS-INC-1), closing the loop required by ISO/IEC 42001's continual-improvement clause.
