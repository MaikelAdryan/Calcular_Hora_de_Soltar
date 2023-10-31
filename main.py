from datetime import timedelta

def calculate_hour_exit(
    journey='7:10', start_journey='',
    start_interval='', end_interval='',
    format_hour= lambda str : [int(i) for i in str.split(':')]
  ):
  hours, minutes = format_hour(journey)
  journey = timedelta(hours, minutes)
  start_journey = timedelta(hours=15, minutes=49)
  start_interval = timedelta(hours=18, minutes=30)
  end_interval = timedelta(hours=18, minutes=50)
  total_interval = end_interval - start_interval
  total_journey = journey + total_interval
  end_journey = start_journey + total_journey
  print(f'Soltará às {end_journey}')
  
calculate_hour_exit()
