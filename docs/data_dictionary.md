# Data Dictionary
 
## Source systems
Field names are the planned names; they are confirmed when the generator is written.
There is no sessions source: sessions are built from events in Silver (decision 5).
 
| Source | Round | Purpose | Format | Grain | Approx. rows | Key fields |
|---|---|---|---|---|---|---|
| app_users.csv | 1 | Product database export of accounts | CSV | 1 per account | ~20,300 | user_id (e.g. u_004821), email, signup_ts, country, platform |
| events.jsonl | 1 | Product event log | JSON lines | 1 per event | ~1,000,000 | event_id, user_id, device_id, event_name, event_ts, received_at, properties |
| billing_customers.csv | 1 | Billing system customers | CSV | 1 per billing customer | ~7,500 | customer_id (e.g. cus_8F2k...), email, product_user_id (often blank) |
| subscriptions.csv | 1 | Billing subscriptions | CSV | 1 per subscription | ~6,500 | subscription_id, customer_id, plan_code, status, started_at, trial_start, trial_end, canceled_at |
| payments.csv | 1 | Billing charge attempts | CSV | 1 per charge attempt | ~35,000 | payment_id, subscription_id, amount, currency, status, livemode, paid_at, platform |
| refunds.csv | 1 | Billing refunds | CSV | 1 per refund | ~1,200 | refund_id, payment_id, amount, refunded_at, reason |
| plan_prices.csv | 1 | Price list with history | CSV | 1 per plan x price version | ~6 | plan_code, price, valid_from, valid_to |
| app_releases.csv | 1 | App release log | CSV | 1 per release | ~50 | platform, version, release_date |
| installs.csv | 2 | Attribution vendor | CSV | 1 per install | ~45,000 | install_id, device_id, channel, campaign, install_ts, platform |
| marketing_spend.csv | 2 | Ad platform spend | CSV | 1 per channel x campaign x day | ~6,500 | date, channel, campaign, spend, impressions, clicks |
| referrals.csv | 3 | Invite system | CSV | 1 per invite | ~8,000 | invite_id, inviter_user_id, invitee_email, sent_at, accepted_at |
| support_tickets.json | 3 | Helpdesk export | JSON array | 1 per ticket | ~4,000 | ticket_id, requester_email, created_at, category, status |
| surveys.csv | 3 | NPS/CSAT tool | CSV | 1 per response | ~6,000 | response_id, user_id, survey_type, score, submitted_at |
 
### Field notes
- `events.received_at`: when the server received the event. Differs from `event_ts` for late-arriving (offline) events.
- `payments.livemode`: true = real payment, false = test payment.
- Identity keys differ by system: product uses user_id, billing uses customer_id,
  support uses email only, attribution uses device_id.
## Source-to-Bronze column mappings
Filled in when Bronze is built.
 