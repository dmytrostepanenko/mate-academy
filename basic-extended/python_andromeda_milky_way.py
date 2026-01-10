distance_light_years = 2.537 * 1_000_000    # світлових років від нашої галактики
distance_km = distance_light_years * 9_461_000_000_000    # Один світловий рік — це приблизно 9.461 трлн кілометрів.
speed_of_light_km_per_s = 300_000

# Розрахуй, скільки часу знадобиться світлу, щоб подолати цю відстань, як у секундах (time_in_seconds), 
# так і у роках (time_in_years). Один рік становить приблизно 31 536 000 секунд (60 * 60 * 24 * 365).

time_in_second = distance_km / speed_of_light_km_per_s
time_in_year = time_in_second / 31536000