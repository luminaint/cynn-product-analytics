# Project State

_Last updated: 2026-09-27_

## Status
Environment setup complete. Repo is on GitHub.

## Done
- Design approved: company, business model, stakeholders, headline problem,
  AARRR KPIs, funnel steps and rules, source systems, fact grains
- Python 3.13.5 venv in `.venv`, created with `py -3.13` (not Anaconda)
- `requirements.txt` with all versions pinned
- VS Code connected to the venv
- Git configured; repo initialized; `.gitignore` in place
- GitHub repo: https://github.com/luminaint/cynn-product-analytics (public, MIT license)

## File tree
    product-analytics-project/
    ├── .venv/              (ignored by Git)
    ├── docs/
    │   ├── PROJECT_STATE.md
    │   └── glossary.md
    ├── .gitignore
    └── requirements.txt

## Key decisions
| # | Decision | Why |
|---|---|---|
| 1 | Company: Ledgerly, freemium budgeting app (iOS, Android, web). Free / Plus Monthly $7.99 / Plus Annual $59.99 / 14-day no-card trial | Clear "aha" moment; weekly usage creates real metric debates |
| 2 | Data window 2025-09-01 to 2026-08-31; as-of date 2026-08-31 | Fixed end date makes results reproducible |
| 3 | Headline problem: 30-day signup-to-paid conversion fell for Jun-Aug 2026 cohorts vs H1 | Tests acquisition vs onboarding vs pricing |
| 4 | Python 3.13 instead of 3.11 | Already installed; 3.11 no longer gets Windows installers |
| 5 | Sessions built from events (30-min inactivity rule), no sessions source file | One definition of a session |
| 6 | Two-part funnel: install->signup (one row per install) + signup->retained paid (one row per user) | Non-signups have no user_id |
| 7 | Strict ordered funnel; step 5 = trial OR direct purchase (flagged) | Keeps step counts testable without losing direct buyers |
| 8 | Windows from signup: onboarding 7d, activation 7d, paid path 14d, paid 30d, retained paid 60d | Matches trial length plus buffer |
| 9 | Activation = linked 1+ bank account AND created 1+ budget within 7 days | App is useless without data; check vs retention later (correlational) |
| 10 | Censored users excluded from denominators; headline funnel uses cohorts at least 60 days old | Otherwise recent cohorts look falsely worse |
| 11 | Pin every package version, including dependencies | Same toolbox on every machine and in CI |
| 12 | Project lives in C:\dev (no spaces, no OneDrive) | Avoids path bugs and file-locking |
| 13 | Merged GitHub's LICENSE commit instead of force-pushing | Keeps the license; force-push deletes the remote's history |
| 14 | Planted stories go in a sealed file (hidden_effects.py) + answer key, written by Claude; I don't open them until my analysis is done | Keeps the analysis a blind investigation |
| 15 | 28 designed imperfections (see data_quality.md); added received_at to events and livemode to payments | Each has a business cause and breaks a named KPI |
## Open issues
- Answer-key secrecy: I type the data generator myself, so I would see the
  planted patterns while typing. Decide how to handle this before data generation.
  - Sealed files (src/generate/hidden_effects.py, docs/answer_key_synthetic.md) are
  delivered by Claude at the data-generation step. Save them without opening.
  If a new chat starts before they exist, Claude designs them fresh; I must not see them.

## Next step
Push the repo to GitHub. Then design data imperfections (spec section 5.2).
Decide how to keep the answer key secret (see Open issues).
Then design data imperfections (5.2) and planted stories (5.3).
Start the data generator in src/generate/: first piece is the config (seed, dates, sizes).


## How to resume work
1. Open VS Code in C:\dev\product-analytics-project
2. Open a terminal; check the prompt shows (.venv) and `python --version` says 3.13.5
3. If not: `.\.venv\Scripts\Activate.ps1`