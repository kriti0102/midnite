with base as (
  select
    u.user_id,
    u."Name",
    u.country_code,
    b.bet_date,
    sum(b.wager_usd) as total_wager_usd,
    sum(b.winnings_usd) as total_winnings_usd,
    count(b.bet_id) as total_bets
  from {{ ref('dim_users') }} u
  join {{ ref('fact_bets') }} b on u.user_id = b.user_id
  join {{ ref('dim_outcomes') }} o on b.bet_outcome_id = o.outcome_id
  group by u.user_id, u."Name", u.country_code, b.bet_date
)

select * from base
