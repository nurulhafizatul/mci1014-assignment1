# 02 Stakeholders and Decision Map

| ID | Stakeholder | Needs | Decision authority | Accountability |
|----|-------------|-------|--------------------|----------------|
| S1 | Student (account holder) | Quick, accurate view of spending vs budget; low effort; privacy | Final authority on budget limits, categories and every purchase | Accountable for acting on advice and for correcting wrong categories |
| S2 | Sponsor / family member | Confidence the allowance is used responsibly; no access to private details | Decides whether to send extra funds; may see only a summary if the student consents | Accountable for emergency funding decisions |
| S3 | Application developer / maintainer (the student acting as developer) | Maintainable, testable, reproducible system; clear logs | Decides model, rules and release of changes | Accountable for correctness, security fixes and documentation |
| S4 | Course lecturer / assessor | Evidence that design decisions are justified and verifiable | Awards marks, approves the evaluation | Accountable for fair assessment |

## Decision map
| Decision | Made by | Supported by AI? | Human oversight |
|----------|---------|------------------|-----------------|
| Set monthly budget and category limits | S1 | No (human only) | n/a |
| Accept or correct a suggested category | S1 | Yes: AI suggests | S1 confirms or edits every low-confidence item |
| Act on a spending warning | S1 | Yes: AI forecasts | S1 can dismiss or tune alerts |
| Share summary with sponsor | S1 | No | S1 explicit opt-in |
| Change the model or rules | S3 | No | Tests must pass in CI before release |
