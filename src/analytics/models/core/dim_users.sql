with base as (
  select
    u.id as user_id,
    u."Name",
    u."CurrencyCode",
    ua.country_code,
    u."CreatedAt" as user_created_at
  from raw.users u
  join raw.user_address ua on u.id = ua.user_id
  where not u."IsTestUser"
    and ua.country_code in ('IE', 'GB')
)

select * from base