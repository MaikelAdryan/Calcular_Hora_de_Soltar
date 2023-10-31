from datetime import timedelta

journey = timedelta(hours=7, minutes=10)

start_journey = timedelta(hours=15, minutes=49)
start_interval = timedelta(hours=17, minutes=30)
end_interval = timedelta(hours=18, minutes=50)
total_interval = end_interval - start_interval
total_journey = journey + total_interval
end_journey = start_journey + total_journey

print(f'Soltará as {end_journey}')
