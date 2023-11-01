from datetime import timedelta, datetime

def transform_in_timedelta(hour):
  hours, minutes = [int(i) for i in str(hour).split(':')]
  return timedelta(hours=hours, minutes=minutes)


def formatting_in_time(time):
  time = str(time) if not type(time) == type('') else time
  time = time.split(', ')[1] if time.count(',') == 1 else time
  time = f'{time}:00' if time.count(':') == 1 else time
  return datetime.strptime(time, "%H:%M:%S").strftime("%H:%M")
# print(formatting_in_time('1 day, 0:49:00')) -> '00:49' print(formatting_in_time('7:10:00')) -> 07:10


def calculate_hour_exit(
    journey='7:10', start_journey='15:49',
    start_interval='17:00', end_interval='17:30'
  ):
  journey = transform_in_timedelta(journey)
  start_journey = transform_in_timedelta(start_journey)
  start_interval = transform_in_timedelta(start_interval)
  end_interval = transform_in_timedelta(end_interval)
  
  total_interval = end_interval - start_interval
  total_journey = journey + total_interval
  end_journey = start_journey + total_journey
  
  return print(
    f'Duração do Intervalo: {formatting_in_time(total_interval)}\n'
    f'Soltará às: {formatting_in_time(end_journey)}'
  )


def formatting_in_hour(time):
  return f'{time[0:2]}:{time[2:4]}' if len(time) == 4 else time
#formatting_time('1520') -> '15:20'


calculate_hour_exit(
  start_journey=formatting_in_hour(input('Início da jornada: ')),
  start_interval=formatting_in_hour(input('Início do intervalo: ')),
  end_interval=formatting_in_hour(input('Fim do intervalo: '))
)
