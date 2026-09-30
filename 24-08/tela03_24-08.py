'''
Faça o programa referente a tela a seguir. Seu programa deve receber o gênero e a altura de uma pessoa e deve calcular seu peso ideal. Programe também os botões Limpar (que limpa o InputText e retorna o Radio ao valor padrão) e o botão Sair (que fecha a aplicação).

Fórmulas:
Homens => Peso Ideal = altura * 72,7 - 58
Mulheres => Peso Ideal = altura * 62,1 – 44,7

Instalação da biblioteca do PySimpleGUI via terminal
larissa>pip3 install FreeSimpleGUI

'''

import FreeSimpleGUI as sg
sg.change_look_and_feel('DarkPurple')

layout = [[sg.Text('Informe o gênero: ')],
          [sg.Radio('Feminino', 'gênero', key='feminino', default=True), sg.Radio('Masculino', 'gênero', key='masculino')],
          [sg.Text(f'Altura')],
          [sg.Input(key='altura')],
          [sg.Text(f'Peso Ideal: ', key='resultado')],
          [sg.Button('Calcular'), sg.Button('Limpar'), sg.Button('Fechar')]]

janela = sg.Window('Peso ideal', layout, resizable=True, size=(500,300))

while True:
  evento, valores = janela.read()

  if evento == sg.WIN_CLOSED or evento == "Fechar":
    break
  if evento == "Calcular":
    if (valores['altura'] == ''):
      sg.popup_ok('Todos os campos devem ser preenchidos!', title='Aviso!')
    else:
      if valores['feminino']:
        janela['resultado'].update(f'Peso ideal: {float(valores['altura'])*62.1 - 44.7}')
      else:
        janela['resultado'].update(f'Peso ideal: {float(valores['altura'])*72.7 - 58}')
  if evento=='Limpar':
    janela['feminino'].update(True)
    janela['resultado'].update(f'Peso ideal: ')
    janela['altura'].update('')




janela.close()