-- models/reporting/game_performance_summary.sql

with game_summary as (
  select
    g.game_name,
    g.vertical,
    b.bet_date,
    count(b.bet_id) as total_bets,
    sum(b.wager_usd) as total_wagered,
    sum(b.winnings_usd) as total_paid_out
  from {{ ref('fact_bets') }} b
  join {{ ref('dim_games') }} g on b.game_id = g.game_id
  group by g.game_name, g.vertical, b.bet_date
)

select * from game_summary
