from datetime import timedelta, datetime

def transform_in_timedelta(hour):
  hours, minutes = [int(i) for i in str(hour).split(':')]
  return timedelta(hours=hours, minutes=minutes)


def format_time(time):
  time = str(time) if not type(time) == type('') else time
  time = time.split(', ')[1] if time.count(',') == 1 else time
  time = f'{time}:00' if time.count(':') == 1 else time
  return datetime.strptime(time, "%H:%M:%S").strftime("%H:%M")
# print(format_time('1 day, 0:49:00')) print(format_time('7:10:00'))


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
    f'Duração do Intervalo: {format_time(total_interval)}\n'
    f'Soltará às: {format_time(end_journey)}'
  )


calculate_hour_exit(
  start_journey=input('Início da jornada: '),
  start_interval=input('Início do intervalo: '),
  end_interval=input('Fim do intervalo: ')
)
