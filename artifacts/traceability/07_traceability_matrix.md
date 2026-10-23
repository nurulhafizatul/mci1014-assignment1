# 07 Traceability Matrix

| Req ID | Problem evidence | Requirement | Architecture component | Risk | Control | Planned verification |
|--------|------------------|-------------|------------------------|------|---------|----------------------|
| REQ-01 | Untracked daily spending, balance near zero on day 23 | Auto-categorise imported transactions (US-01) | Categoriser | R-01 | 70% confidence threshold, review queue | Test on 100 labelled transactions (AC-01a) |
| REQ-02 | Student must stay in control of decisions | Flag low-confidence items for human review (QAS-01) | Human Review Queue | R-01, R-03 | Override in 2 clicks, corrections stored | Manual walkthrough and UI test (AC-01b) |
| REQ-03 | Sensitive financial data used | Mask account data before any external call (QAS-03) | Import and Masking Service | R-02 | Masking, encryption at rest | Unit test on outbound payload |
| REQ-04 | AI may fail; non-AI baseline exists | Fallback to rule-based categoriser (QAS-02) | Categoriser (rule fallback) | R-04 | Keyword rules | Simulated model failure test |
| REQ-05 | Sponsor needs limited visibility | Opt-in category-only summary (US-02) | UI, Encrypted store | R-05 | Consent toggle, aggregation only | AC-02a, AC-02b |
| REQ-06 | Month-end shortfall | Forecast month-end balance with warning (US-01) | Forecast and Alert Engine | R-03 | Range display, disclaimer | Forecast test against last month's data |
| REQ-07 | Work must be verifiable by assessor | Reproducible repo and automated checks (US-03, US-04, QAS-04) | GitHub Actions, validator | R-06 | CI quality gate | Green artifact-check run (AC-03a, AC-03b) |
