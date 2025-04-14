WITH fx AS (
  SELECT
    date,
    currency_code,
    rate
  FROM raw.fx_rates
),

bets AS (
  SELECT
    b.id AS bet_id,
    b.user_id,
    b.bet_outcome_id,
    b.game_id,
    b.wager,
    b.winnings,
    b.created_at::date AS bet_date,
    b.settled_at::date AS settled_date,
    u."CurrencyCode",
    COALESCE(fx.rate, 1.0) AS fx_rate,  -- Use 1.0 if fx rate is missing
    b.wager * COALESCE(fx.rate, 1.0) AS wager_usd,
    b.winnings * COALESCE(fx.rate, 1.0) AS winnings_usd,
    b.is_cash_wager
  FROM raw.bet b
  JOIN {{ ref('dim_users') }} u ON b.user_id = u.user_id
  LEFT JOIN fx ON fx.date = b.created_at::date AND fx.currency_code = u."CurrencyCode"
)

SELECT * FROM bets
