# Crosswalk: ISO/IEC 42001:2023 ↔ NIST AI Risk Management Framework

Derived from [`controls/ai-controls.yaml`](../controls/ai-controls.yaml). Each row is a single source-of-truth AI control, shown against its ISO 42001 references and the NIST AI RMF functions/subcategories it satisfies. Regenerate this view when the catalog changes — do not hand-edit mappings here.

The NIST AI RMF organizes around four functions — **GOVERN, MAP, MEASURE, MANAGE** — while ISO/IEC 42001 is a certifiable management-system standard with Annex A controls. They are complementary: 42001 gives you the auditable system; the AI RMF gives you the risk-reasoning vocabulary. Mapping once lets one implementation answer both.

| Catalog ID | Control | ISO 42001 | NIST AI RMF |
|------------|---------|-----------|-------------|
| AIMS-GOV-1 | AI Policy and Accountability | Clause 5.2, A.2.2, A.2.3 | GOVERN-1.1, GOVERN-2.1 |
| AIMS-DATA-1 | Training Data Governance | A.7.2, A.7.3, A.7.4 | MAP-2.3, MEASURE-2.2 |
| AIMS-RISK-1 | AI Risk Assessment and Impact Analysis | Clause 6.1, A.5.2, A.5.4 | MAP-1.1, MEASURE-2.1, MANAGE-1.1 |
| AIMS-VAL-1 | Model Validation and Performance Testing | A.6.2, A.8.2 | MEASURE-2.3, MEASURE-2.5, MEASURE-2.11 |
| AIMS-OVS-1 | Human Oversight of AI Decisions | A.9.2, A.9.3 | GOVERN-1.2, MANAGE-2.2 |
| AIMS-TRANS-1 | Transparency and System Documentation | A.8.3, A.8.4 | GOVERN-4.2, MAP-3.4 |
| AIMS-MON-1 | Operational Monitoring and Drift Detection | A.9.3, A.9.4 | MANAGE-4.1, MEASURE-2.6 |
| AIMS-INC-1 | AI Incident Response and Reporting | A.10.2, A.10.3 | MANAGE-4.1, MANAGE-4.3 |

**Reading the crosswalk:** the catalog control is the unit of truth; ISO 42001 and the AI RMF are two views onto it. A single implementation and its evidence answer both a 42001 certification audit and an AI-RMF-aligned risk review.

*ISO Annex A and AI RMF references are summarized, not quoted. Mappings are illustrative and synthetic.*
