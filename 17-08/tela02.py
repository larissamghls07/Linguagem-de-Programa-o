'''
Faça o programa referente a tela a seguir. Seu programa deve receber os preços da gasolina e do etanol e avaliar se é melhor abastecer com Etanol, Gasolina ou com Etanol ou Gasolina (tanto faz). Para isso considere que o Etanol rende apenas 70% da gasolina. Programe também os botões Limpar (que retorna os InputText e o Text e para o estado original) e o botão sair (que fecha a aplicação).

Obs.: Contemple em seu programa a verificação se há conteúdo nas caixas dos preços da gasolina e do etanol antes de fazer o cálculo.
'''

import FreeSimpleGUI as sg
sg.change_look_and_feel('BrightColors')

#definição das componentes 
lista = [[sg.Text('Preço da Gasolina: '), sg.Input(key="gasolina")],
         [sg.Text('Preço do Etanol: '), sg.Input(key="etanol")],
         [sg.Text('Abasteça: ', key="resultado")],
         [sg.Button('Calcular'), sg.Button('Limpar'), sg.Button('Sair')]]

janela = sg.Window('Combustíveis', lista)

while True:
  event, valores = janela.read()
  if event == sg.WIN_CLOSED or event == "Sair":
    break
  if event == 'Calcular':
    if (valores['etanol'] == '') or valores['gasolina'] == "":
      janela['resultado'].update(f'Todos os campos devem ser preenchidos!')
    else:
      preco_gasolina = float(valores['gasolina'])
      preco_etanol = float(valores['etanol'])

      if preco_etanol > preco_gasolina:
        janela['resultado'].update(f'Abasteça com gasolina, está {preco_etanol - preco_gasolina} mais barato.')
      else:
        janela['resultado'].update(f'Abasteça com etanol.')
  if event == "Limpar":
    janela['gasolina'].update('')
    janela['etanol'].update('')
    janela['resultado'].update(f'Abasteça:')

janela.close()
