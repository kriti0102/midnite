-- models/sources/staging_bets.sql

with bets as (
  select
    id as bet_id,
    user_id,
    bet_outcome_id,
    game_id,
    wager,
    is_cash_wager,
    winnings,
    created_at,
    settled_at
  from raw.bet
)

select * from bets
