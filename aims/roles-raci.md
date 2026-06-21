# AI Governance RACI

*Synthetic example. Maps accountability for AIMS activities across roles. R = Responsible, A = Accountable, C = Consulted, I = Informed.*

| Activity | AI Gov Lead | System Owner | Data Science | Security (CISO) | Legal/Privacy | Leadership |
|----------|:-----------:|:------------:|:------------:|:---------------:|:-------------:|:----------:|
| Approve AI policy | R | I | I | C | C | A |
| Maintain AI system inventory | A | R | C | I | I | I |
| Risk & impact assessment ([AIMS-RISK-1]) | A | R | C | C | C | I |
| Training-data governance ([AIMS-DATA-1]) | C | A | R | C | C | I |
| Model validation ([AIMS-VAL-1]) | C | A | R | I | I | I |
| Human-oversight design ([AIMS-OVS-1]) | A | R | C | C | C | I |
| Operational monitoring ([AIMS-MON-1]) | C | A | R | C | I | I |
| AI incident response ([AIMS-INC-1]) | C | R | C | A | C | I |
| AIMS internal audit & review | A | C | C | C | C | I |

**Reading it:** every activity has exactly one **A** (single point of accountability) — the test a 42001 assessor applies first. Security (CISO) is accountable for AI *incident response*, reflecting that AI incidents route through the existing IR capability (see the [42001 ↔ 27001 crosswalk](../crosswalks/42001_to_27001.md)), while the AI Governance Lead owns the governance and assurance activities.

[AIMS-RISK-1]: ../controls/ai-controls.yaml
[AIMS-DATA-1]: ../controls/ai-controls.yaml
[AIMS-VAL-1]: ../controls/ai-controls.yaml
[AIMS-OVS-1]: ../controls/ai-controls.yaml
[AIMS-MON-1]: ../controls/ai-controls.yaml
[AIMS-INC-1]: ../controls/ai-controls.yaml
