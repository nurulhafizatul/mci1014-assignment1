# 06 Initial Risk Register

Scale: Likelihood and Impact = Low / Medium / High.

| ID | Risk | Affected stakeholder | Consequence | Likelihood | Impact | Control | Owner | Evidence |
|----|------|----------------------|-------------|------------|--------|---------|-------|----------|
| R-01 | Wrong auto-categorisation (e.g. "Grab" food vs ride) | S1 | Misleading budget, poor spending decision | High | Medium | Confidence threshold 70%, human review queue, store corrections | Developer (S3) | Test report on 100 sample transactions; AC-01a |
| R-02 | Financial data leaked to external LLM or storage | S1, S2 | Privacy breach, loss of trust | Medium | High | Masking before external calls, encryption at rest, secrets scan | Developer (S3) | Masking unit test; QAS-03 result |
| R-03 | Over-reliance on forecast | S1 | Student ignores real balance and overspends | Medium | Medium | Show forecast as range with disclaimer; weekly manual balance check prompt | Student (S1) | Usability check of dashboard text |
| R-04 | AI service outage or API cost change | S1, S3 | App unusable | Medium | Medium | Rule-based fallback categoriser | Developer (S3) | Fallback test; QAS-02 |
| R-05 | Sponsor sees more than consented | S2, S1 | Privacy violation, family conflict | Low | High | Opt-in consent, summary shows category totals only | Student (S1) | AC-02a, AC-02b tests |
| R-06 | Repository missing or broken artifacts | S3, S4 | Cannot be verified or assessed | Medium | High | CI artifact-check workflow and local validator | Developer (S3) | Green GitHub Actions run |
