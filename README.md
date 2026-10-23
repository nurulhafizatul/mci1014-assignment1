# MCI1014 Assignment 1 - AI-Assisted Monthly Student Budget Categoriser

**Course:** Artificial Intelligence in Software Engineering (MCI1014), UMPSA
**Student:** <YOUR NAME> (<YOUR MATRIC NO>)
**Semester:** Session 2025/2026 II

## Selected case study
A student on a fixed monthly allowance runs out of money before month end because spending across e-wallets, bank transfers and cash is not tracked. This repository holds the pre-development artifacts for a proposed AI-enabled budget categoriser, including a non-AI alternative (manual envelope spreadsheet) and a human review step for every uncertain decision.

## Repository structure
```
README.md
artifacts/
  docs/          01 problem, 02 stakeholders, 03 user stories, 04 quality scenarios, 05 architecture
  risks/         06 risk register
  traceability/  07 traceability matrix
tools/           validate_artifacts.py
.github/workflows/artifact-check.yml
```

## Environment check and reproducible instructions
Requirements: Python 3.9 or newer (tested with 3.11). No external packages are needed.

```bash
git clone <YOUR REPOSITORY URL>
cd <repository-folder>
python --version
python tools/validate_artifacts.py
```
Expected output: `ALL CHECKS PASSED`. The same command runs automatically on GitHub through the `artifacts-check` workflow on every push (see the Actions tab). In Google Colab, upload the folder and run `!python tools/validate_artifacts.py`.

## AI-use declaration
Generative AI (Claude, by Anthropic) was used to help produce a first draft of the artifacts and the validator script. Per the assignment rules, each use is declared below. **Replace the placeholders with your real prompts and your own justification before submitting.**

| # | Prompt used (summary) | AI output used | Adopted? | My justification / edits |
|---|-----------------------|----------------|----------|--------------------------|
| 1 | Uploaded assignment brief; asked for help understanding the task and creating the repository for the problem "monthly student budgeting" | Drafts of artifacts 01-07, README, validate_artifacts.py, artifact-check.yml | Yes, after review | <Write what you checked and changed, e.g. adjusted figures to my own real spending, edited risks> |
| 2 | <Add any further prompts you used> | <output> | <Yes/No> | <reason> |

Full prompts and outputs are included in the evidence ZIP.
