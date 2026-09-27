
Project state · MD
# Project State
 
_Last updated: 2026-09-27_
 
## Status
Design and environment setup complete. Repo is on GitHub.
Build approach: thin slice first (Round 1 end to end, then Rounds 2 and 3).
 
## Done
- Design approved: company, business model, stakeholders, headline problem,
  AARRR KPIs, funnel steps and rules, source systems, fact grains
- 28 data imperfections designed (docs/data_quality.md)
- Python 3.13.5 venv in `.venv`, created with `py -3.13` (not Anaconda)
- `requirements.txt` with all versions pinned
- VS Code connected to the venv
- Git configured; GitHub repo: https://github.com/luminaint/cynn-product-analytics (public, MIT license)
- Generator settings file: src/generate/config.py (seed 42, date window, 20,000 users, output folder)
## File tree
    product-analytics-project/
    ├── .venv/              (ignored by Git)
    ├── docs/
    │   ├── PROJECT_STATE.md
    │   ├── data_dictionary.md
    │   ├── data_quality.md
    │   └── glossary.md
    ├── src/
    │   └── generate/
    │       └── config.py
    ├── .gitignore
    ├── LICENSE
    └── requirements.txt
 
## Build rounds
| Round | Sources | Delivers |
|---|---|---|
| 1 | app_users, events, billing_customers, subscriptions, payments, refunds, plan_prices, app_releases | Bronze, Silver, Gold; user funnel; activation; retention; engagement; MRR, churn, ARPU; tests; CI |
| 2 | installs, marketing_spend | Install-to-signup funnel; channel mix; CAC, LTV:CAC, payback; root cause; dashboard; memo |
| 3 | referrals, support_tickets, surveys | Stretch KPIs: K-factor, NPS, CSAT |
 
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
| 16 | Thin slice first: build Round 1 end to end before Rounds 2-3 | Presentable project at about the halfway point |
| 17 | MRR is calculated from subscriptions x plan price, not from payments | MRR = what customers are subscribed to pay; cash revenue is a separate metric |
 
## Open issues
- Sealed files (src/generate/hidden_effects.py, docs/answer_key_synthetic.md) are
  delivered by Claude at the data-generation step. Save them without opening.
  If a new chat starts before they exist, Claude designs them fresh; I must not see them.
## Next step
Round 1 generator: src/generate/users.py (create the clean list of real users).
 
## How to resume work
1. Open VS Code in C:\dev\product-analytics-project
2. Open a terminal; check the prompt shows (.venv) and `python --version` says 3.13.5
3. If not: `.\.venv\Scripts\Activate.ps1`
4. Keep File > Auto Save turned on, so Git always sees what's on screen