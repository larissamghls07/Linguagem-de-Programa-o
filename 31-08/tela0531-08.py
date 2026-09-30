import FreeSimpleGUI as sg

sg.change_look_and_feel('DarkPurple')

def notas():
  sg.change_look_and_feel('DarkPurple')
  opcoes = ['Redes III','Sistema Operacional I','Filosofia da Técnica']

  layout = [[sg.Text(f'Nome de aluno: ')],
            [sg.Input(key='nome')],
            [sg.Text(f'Disciplina: ', key='disciplina'), sg.Combo(opcoes,default_value='Escolha a disciplina', readonly=True, key='combo')],
            [sg.Text(f'Nota 1: '), sg.Text(f'Nota 2: '), sg.Text('Média'), sg.Text('Resultado')],
            [sg.Input(key='nota1', size=(7)), sg.Input(key='nota2', size=(7)), sg.Text(key='media', size=(5)), sg.Text(key='resultado')],
            [sg.Button('Calcular'), sg.Button('Limpar'), sg.Button('Fechar')]]


  janela = sg.Window('Formulário de notas', layout, resizable=True, size=(500,300))

  while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == "Fechar":
      break
    if evento == 'Calcular':
      media = (float(valores['nota1']) + float(valores['nota2']))/2
      janela['media'].update(media)


      if media >= 6:
        janela['resultado'].update(f'Aprovado!')
      elif media <= 4:
        janela['resultado'].update(f'Reprovado direto!')
      elif 4 < media < 6:
        janela['resultado'].update(f'Recuperação!')


    if evento=='Limpar':
      janela['nota1'].update('')
      janela['nota2'].update('')
      janela['media'].update('')
      janela['nome'].update('')
      janela['combo'].update(value='Escolha a disciplina')
      janela['resultado'].update('')


  janela.close()


def pesoideal():
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


def combustivel():
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




menu_def = [
  ['Opções de conversores',['Temperatura','Combustível','Peso Ideal']],
  ['Outras opções',['Ajuda com os conversores','Notas']]
]


layout = [
  [sg.Menu(menu_def, key='menuprincipal')],
  [sg.Text(f'Sistema Princial para visualização.', font=('Times New Roman',14), justification='center', expand_x=True)],
  [sg.Text(f'Vá até o menu disponível na aba superior à esquerda.', font=('Times New Roman',14), justification='center', expand_x=True)]
]

janela = sg.Window('Menu de funções para conversão!', layout)

while True:
  evento, valores = janela.read()

  if evento == sg.WIN_CLOSED or evento == "Fechar":
    break
  elif evento == 'Combustível':
    combustivel()
  elif evento == 'Peso Ideal':
    pesoideal()
  elif evento == 'Notas':
    notas()



janela.close()