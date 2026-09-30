import FreeSimpleGUI as sg
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

