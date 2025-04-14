-- models/reporting/daily_revenue.sql

with revenue as (
  select
    b.bet_date,
    sum(b.wager_usd - b.winnings_usd) as revenue_usd
  from {{ ref('fact_bets') }} b
  group by b.bet_date
)

select * from revenue
