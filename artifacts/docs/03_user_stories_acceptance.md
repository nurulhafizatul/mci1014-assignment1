# 03 User Stories and Acceptance Criteria

## US-01 (Student, S1)
As a student, I want my transactions automatically categorised so that I can see my spending vs budget without manual data entry.

- **AC-01a**: Given a CSV export of 100 transactions, When I import it, Then at least 85 are assigned the correct category and every item with confidence below 70% is flagged "Needs review".
- **AC-01b**: Given a flagged transaction, When I choose a category, Then the dashboard updates within 2 seconds and the choice is stored as a correction.

## US-02 (Sponsor, S2)
As a sponsor, I want an optional monthly summary of total spent per category so that I can judge whether extra support is needed, without seeing individual transactions.

- **AC-02a**: Given the student has not enabled sharing, When the sponsor requests a summary, Then no data is shown.
- **AC-02b**: Given sharing is enabled, When the summary is generated, Then it contains only category totals and no merchant names or transaction rows.

## US-03 (Developer, S3)
As the developer, I want automated checks and a reproducible environment so that I can change the categoriser safely.

- **AC-03a**: Given a clean clone, When I run `python tools/validate_artifacts.py`, Then it exits with code 0 and prints "ALL CHECKS PASSED".
- **AC-03b**: Given a push to GitHub, When the artifact-check workflow runs, Then it finishes green in under 3 minutes, and fails if any artifact file is missing.

## US-04 (Lecturer, S4)
As an assessor, I want each requirement linked to evidence so that I can verify the design is justified.

- **AC-04a**: Given the traceability matrix, When I pick any requirement, Then I can find its problem evidence, architecture component, risk, control and planned verification in one row.
