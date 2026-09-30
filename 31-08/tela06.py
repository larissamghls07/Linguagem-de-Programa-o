import FreeSimpleGUI as sg

sg.change_look_and_feel('DarkPurple')

autor = ['Stephen King','Elena Ferrante','Raphael Montes']
genero = ['Romance policial','Suspense psicológico','Romance histórico']


coluna_capadura = [
  [sg.Text('Capa dura ')],
  [sg.Radio('Sim', 'estilodecapa', key='sim', default=True), sg.Radio('Não', 'estilodecapa', key='nao')] 
]

coluna_formato = [
  [sg.Text('Formato')],
  [sg.Checkbox('EPUB', default=True, key='epub'), sg.Checkbox('MOBI', key='mobi'), sg.Checkbox('Físico', key='fisico')]
]

coluna_autor = [
  [sg.Text('Autor: ')],
  [sg.Combo(autor, default_value='Escolha o autor', readonly=True, key='autorcombo')]
]

coluna_genero = [
  [sg.Text('Gênero: ')],
  [sg.Combo(genero, default_value='Escolha o gênero', readonly=True, key='generocombo')]
]

layout = [
  [sg.Text(f'ISBN', font=('Times New Roman',14), justification='left', expand_x=True)],
  [sg.Input(key='isbn'), sg.Button('Buscar', disabled=False)],
  [sg.Text(f'Título: ', font=('Times New Roman',14), justification='left', expand_x=True)],
  [sg.Input(key='titulo')],
  [sg.Column(coluna_autor, pad=(0,0), element_justification='left'), sg.Column(coluna_genero, pad=(20,0), element_justification='left')],
  [sg.Column(coluna_capadura, pad=(0,0), element_justification='left'), sg.Column(coluna_formato, pad=(20,0), element_justification='left')],
  [sg.Button('Novo'), sg.Button('Salvar'), sg.Button('Cancelar'), sg.Button('Excluir'), sg.Button('Fechar')]
]

janela = sg.Window('Cadastro de livros', layout)

while True:
  evento, valores = janela.read()

  if evento == sg.WIN_CLOSED or evento == "Fechar":
    break
  elif evento == 'Cancelar':
    janela['isbn'].update('')
    janela['titulo'].update('')
    janela['autorcombo'].update(value='Escolha o autor')
    janela['generocombo'].update(value='Escolha o gênero')
  elif evento == 'Buscar':
    if len(valores['isbn']) > 13:
      sg.popup(f'Você digitou mais números que o permitido!')
      janela['isbn'].update('')



janela.close()

