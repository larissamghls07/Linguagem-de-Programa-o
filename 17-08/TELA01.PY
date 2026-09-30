# comando usado para importar a biblioteca 
import FreeSimpleGUI as sg 

#definição das componentes da janela 
layout = [[sg.Text('Informe a temperatura em Celsius: ')],
          [sg.Input(key="var_celsius")],
          [sg.Text('Temperatura em Fahrenheit:', key="var_fah")],
          [sg.Text('Temperatura em Kelvin:', key="var_kelvin")],
          [sg.Button('Converter'),sg.Button('Limpar'),sg.Button('Fechar')]]

#criação da janela com o layout que foi descrito no vetor acima. 
#Esse vetor é o que estrutura a janela a ser montada
janela = sg.Window('Conversor de temperatura', layout)

#Manipulação dos eventos e valores das variáveis (componentes). 
#Leitura do comportamento do usuário, a interação em relação à janela (evento). 

while True:
  event, values = janela.read()
#se o usuário clicar no X ou através do botão Fechar, o programa sai do laço e fecha a aplicação
  if event == sg.WIN_CLOSED or event == 'Fechar':
    break
  if event == "Converter":
    fah = float(values['var_celsius']) * 1.8 + 32
    janela['var_fah'].update(f'Temperatura em Fahrenheit: {fah}')
    kelvin = float(values['var_celsius']) + 273
    janela['var_kelvin'].update(f'Temperatura em Kelvin: {kelvin}')
  if event == 'Limpar':
    janela['var_fah'].update(f'Temperatura em Fahrenheit:')
    janela['var_kelvin'].update(f'Temperatura em Kelvin:')
    janela['var_celsius'].update('')
    

janela.close()