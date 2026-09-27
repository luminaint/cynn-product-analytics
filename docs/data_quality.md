# Data Quality

## Designed imperfections (known issues planted in the synthetic data)
Profiling must detect and measure each of these. "Ambiguous" items get a
documented rule in decision_log.md during Silver.

Numbers never change, even though marketing (13-18) is built in Round 2,
so later docs can safely refer to "imperfection #23".

### Round 1: Product (app_users, events)
| # | Source | Imperfection | Why it happens | Scale | What breaks if ignored |
|---|---|---|---|---|---|
| 1 | app_users | Same user_id appears twice | Nightly export job retried and overlapped pages | ~0.5% | Signups double-counted |
| 2 | app_users | Emails with mixed case and extra spaces | No cleanup at signup | ~15% | Email matching to billing/support fails |
| 3 | app_users | Messy labels: US/USA/United States/blank; iOS/ios/ANDROID | Old app versions had free-text fields; client teams log differently | ~10% | One segment splits into several |
| 4 | app_users | Internal and test accounts (@ledgerly.com, qa+) | Employees and QA use production | ~150 | Inflates signups; free employee Plus distorts conversion |
| 5 | app_users | Signup date 1970-01-01 | Migration bug wrote a default date where missing | ~20 rows | Breaks cohorts and date ranges |
| 6 | events | Same event_id sent twice | App retries when the network drops | ~2% | Inflates activity and feature adoption |
| 7 | events | Late arrivals: received_at days after event_ts | Phones offline, sync later | ~3% | Latest days look artificially low |
| 8 | events | Mixed timestamp formats (UTC Z, local offsets, epoch ms) | Different app versions | varies | Wrong ordering, sessions, and days |
| 9 | events | Events before signup or in the future | Wrong device clocks | ~0.3% | Impossible funnel ordering |
| 10 | events | Event name drift: budget_created vs BudgetCreated | App v3 renamed events | ~25% of affected events | Activation undercounted |
| 11 | events | user_id not found in users (orphans) | Accounts deleted on request; events kept | ~0.5% | Rows silently vanish in joins |
| 12 | events | Bot accounts with thousands of inhumanly fast events | Automated scripts hitting the web app | ~25 accounts | Inflates DAU and events |

Not an error: events with empty user_id but a device_id are anonymous pre-signup activity.

### Round 1: Billing (billing_customers, subscriptions, payments, refunds)
| # | Source | Imperfection | Why it happens | Scale | What breaks if ignored |
|---|---|---|---|---|---|
| 19 | billing_customers | product_user_id stored as 4821 instead of u_004821, and often blank | Web purchases made before the billing integration | ~35% blank | Identity resolution needs email fallback |
| 20 | billing_customers | One person with two customer_ids | Re-subscribing created a new customer record | ~3% | Customers double-counted |
| 21 | subscriptions | Status labels canceled/cancelled/Canceled | Billing API version change | ~5% | Churn split across labels |
| 22 | subscriptions | Ambiguous: overlapping subscriptions on monthly-to-annual upgrade | Old plan ends as the new one starts | ~4% | Churn + new, or expansion? Changes MRR movements |
| 23 | payments | Same payment_id twice | Payment notification delivered twice | ~1% | Cash revenue double-counted (ARPU, LTV, ROAS too high) |
| 24 | payments | Failed and test payments (livemode = false) mixed in | Normal billing export | ~8% | Revenue inflated |
| 25 | payments | Ambiguous: some refunds recorded as negative payments | Support refunded manually in billing dashboard | ~60 rows | Refunds subtracted twice or not at all |
| 26 | refunds | Refund whose payment is not in payments.csv | Original payment was before the data window | ~2% | Orphan; revenue reconciliation fails |

### Round 2: Marketing (installs, marketing_spend)
| # | Source | Imperfection | Why it happens | Scale | What breaks if ignored |
|---|---|---|---|---|---|
| 13 | installs | Ambiguous: same device_id with several installs | Reinstalls | ~6% | Which install gets credit? Inflates installs, CPI |
| 14 | installs | Channel renamed mid-year (facebook to meta_ads) | Attribution vendor migration | half the year | One channel looks like two |
| 15 | marketing_spend | Same channel and day sent twice | Connector re-sent a report | ~1% | Doubles spend, CAC too high |
| 16 | marketing_spend | Affiliate spend in cents, others in dollars | Affiliate network export format | 1 channel | That channel's CAC 100x too high |
| 17 | marketing_spend | Ambiguous: negative spend rows | Ad-platform credits for faulty delivery | ~20 rows | Legitimate credit or error? |
| 18 | marketing_spend | Channel names differ from installs file | Different systems | all rows | CAC by channel impossible without a mapping |

### Round 3: Feedback (surveys, support_tickets)
| # | Source | Imperfection | Why it happens | Scale | What breaks if ignored |
|---|---|---|---|---|---|
| 27 | surveys | CSAT scored 1-10 instead of 1-5 for two weeks | Survey tool misconfigured | ~150 rows | Impossible CSAT scores |
| 28 | support_tickets | Requester email matches no user | Different email address, or prospects | ~12% | Unmatched tickets need a documented rule |

Clean on purpose: plan_prices.csv, app_releases.csv (internal config data).

## Coverage of required imperfection types
nulls (3, 19) · duplicate records (1, 6, 15, 23) · inconsistent labels (2, 3, 21) ·
invalid dates (5) · timezone mix-ups (8) · impossible values (9, 16, 27) ·
orphan keys (11, 26) · duplicate business keys (13, 20) · inconsistent IDs (19) ·
cancelled/refunded (21, 24, 25) · late-arriving (7) · multiple systems (19, 20, 28) ·
test accounts (4, 24) · bots (12) · ambiguous (13, 17, 22, 25)