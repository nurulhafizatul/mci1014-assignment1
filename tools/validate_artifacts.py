#!/usr/bin/env python3
"""Validate that all required assignment artifacts exist and meet minimum content rules.

Run locally or in Colab:  python tools/validate_artifacts.py
Exit code 0 = all checks passed, 1 = at least one check failed.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "artifacts"

REQUIRED_FILES = {
    "problem": ART / "docs" / "01_problem_statement.md",
    "stakeholders": ART / "docs" / "02_stakeholders_decision_map.md",
    "stories": ART / "docs" / "03_user_stories_acceptance.md",
    "qas": ART / "docs" / "04_quality_attribute_scenarios.md",
    "architecture": ART / "docs" / "05_architecture.md",
    "risks": ART / "risks" / "06_risk_register.md",
    "traceability": ART / "traceability" / "07_traceability_matrix.md",
    "readme": ROOT / "README.md",
}

errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def read(key):
    p = REQUIRED_FILES[key]
    return p.read_text(encoding="utf-8") if p.exists() else ""


# 1. Files exist and are not empty
for key, path in REQUIRED_FILES.items():
    check(path.exists() and path.stat().st_size > 100, f"Missing or empty file: {path.relative_to(ROOT)}")

# 2. Problem statement contains required sections
problem = read("problem").lower()
for section in ["problem description", "problem owner", "affected users", "decision to support",
                "observable value", "possible harm", "non-ai alternative"]:
    check(section in problem, f"Problem statement missing section: {section}")

# 3. At least 3 stakeholders
stake_rows = [l for l in read("stakeholders").splitlines() if re.match(r"\|\s*S\d+\s*\|", l)]
check(len(stake_rows) >= 3, f"Need >= 3 stakeholders, found {len(stake_rows)}")

# 4. At least 3 user stories, each with Given/When/Then
stories = read("stories")
story_count = len(re.findall(r"^## US-\d+", stories, flags=re.M))
check(story_count >= 3, f"Need >= 3 user stories, found {story_count}")
check(len(re.findall(r"\bGiven\b", stories)) >= story_count, "Each user story needs a Given criterion")
check(len(re.findall(r"\bWhen\b", stories)) >= story_count, "Each user story needs a When criterion")
check(len(re.findall(r"\bThen\b", stories)) >= story_count, "Each user story needs a Then criterion")

# 5. At least 4 quality attribute scenarios
qas_count = len(re.findall(r"^## QAS-\d+", read("qas"), flags=re.M))
check(qas_count >= 4, f"Need >= 4 quality scenarios, found {qas_count}")

# 6. Architecture mentions key elements
arch = read("architecture").lower()
for term in ["human oversight", "design rationale", "data flows", "external", "```mermaid"]:
    check(term in arch, f"Architecture missing: {term}")

# 7. At least 4 risks, with required columns
risks = read("risks")
risk_rows = [l for l in risks.splitlines() if re.match(r"\|\s*R-\d+\s*\|", l)]
check(len(risk_rows) >= 4, f"Need >= 4 risks, found {len(risk_rows)}")
for col in ["affected stakeholder", "consequence", "likelihood", "impact", "control", "owner", "evidence"]:
    check(col in risks.lower(), f"Risk register missing column: {col}")

# 8. Traceability matrix rows and columns
trace = read("traceability")
trace_rows = [l for l in trace.splitlines() if re.match(r"\|\s*REQ-\d+\s*\|", l)]
check(len(trace_rows) >= 4, f"Need >= 4 traceability rows, found {len(trace_rows)}")
for col in ["problem evidence", "requirement", "architecture component", "risk", "control", "planned verification"]:
    check(col in trace.lower(), f"Traceability matrix missing column: {col}")

# 9. README has required sections
readme = read("readme").lower()
for section in ["reproduc", "ai-use declaration", "environment"]:
    check(section in readme, f"README missing section containing: {section}")

# 10. Environment check
check(sys.version_info >= (3, 9), f"Python 3.9+ required, found {sys.version.split()[0]}")

if errors:
    print("CHECKS FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("ALL CHECKS PASSED")
print(f"  stakeholders={len(stake_rows)} stories={story_count} qas={qas_count} "
      f"risks={len(risk_rows)} trace_rows={len(trace_rows)}")
sys.exit(0)
