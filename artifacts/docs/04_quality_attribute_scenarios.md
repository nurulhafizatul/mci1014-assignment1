# 04 Quality Attribute Scenarios

Format: Source - Stimulus - Environment - Artifact - Response - Response measure.

## QAS-01 Human-centered operation
- **Source**: Student
- **Stimulus**: The categoriser is unsure about a transaction (confidence < 70%).
- **Environment**: Normal operation during monthly import.
- **Artifact**: Categorisation module and review screen.
- **Response**: The item is flagged "Needs review" and never silently auto-accepted; the student can override in one action.
- **Measure**: 100% of low-confidence items are flagged; override takes at most 2 clicks.

## QAS-02 Reliability
- **Source**: Student
- **Stimulus**: The AI model is unavailable or errors out.
- **Environment**: Runtime, any time.
- **Artifact**: Categorisation module.
- **Response**: Fall back to the rule-based keyword categoriser (the non-AI alternative) and show a notice.
- **Measure**: The import still completes; at least 95% of requests return a result within 5 seconds.

## QAS-03 Security / privacy
- **Source**: External attacker or curious third party
- **Stimulus**: Attempts to read stored transactions or sends them to an external service.
- **Environment**: Deployed app with local storage and an optional external LLM API.
- **Artifact**: Data store and API gateway.
- **Response**: Data encrypted at rest, merchant names and account numbers masked before any external call, no secrets in the repository.
- **Measure**: 0 secrets detected by repository scan; 0 raw account numbers in outbound payload logs.

## QAS-04 Reproducibility
- **Source**: Developer or assessor
- **Stimulus**: Clones the repository on a new machine or Colab.
- **Environment**: Clean Python 3.11 environment.
- **Artifact**: Repository, requirements and validator script.
- **Response**: Setup and validation run from the README steps alone.
- **Measure**: Validator passes in under 2 minutes with no manual fixes.

## QAS-05 Maintainability
- **Source**: Developer
- **Stimulus**: Adds a new spending category.
- **Environment**: Development.
- **Artifact**: Category configuration file.
- **Response**: Category is added by editing configuration only, without changing core code.
- **Measure**: Change completed in under 30 minutes with all checks green.
