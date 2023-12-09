import PySimpleGUI as sg
from main import calculate_hour_exit

sg.theme('Black')
layout = [
  [sg.Text('Calcular horário de saída.')],
  [sg.Text('Carga Horária:', size=(13,1)),
    sg.Input('07:10', size=(5,1), key='journey')],
  [sg.Text('Início da Jornada:', size=(13,1)),
    sg.Input('15:49', size=(5,1), key='start_journey')],
  [sg.Text('Início do Intervalo:', size=(13,1)),
    sg.Input('17:00', size=(5,1), key='start_interval')],
  [sg.Text('Fim do Intervalo:', size=(13,1)),
    sg.Input('17:30', size=(5,1), key='end_interval')],
  [sg.Button('Calcular'), sg.Button('Cancelar')],
  [sg.Text('', key='result')]
]

window = sg.Window('Feito por Adryan!', layout)
while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED or event == 'Cancelar':
    break
  
  if event == 'Calcular':
    hour_exit = calculate_hour_exit(
      journey=values['journey'],
      start_journey=values['start_journey'],
      start_interval=values['start_interval'],
      end_interval=values['end_interval']
    )
    window['result'].update(f'{hour_exit}')

window.close()
