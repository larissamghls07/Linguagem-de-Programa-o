import FreeSimpleGUI as sg

sg.change_look_and_feel('DarkPurple')

estado = ['RJ','SP','MG','ES']
cidade = ['Duque de Caxias','Prainha','Nova Friburgo']


coluna_email = [
  [sg.Text(f'Email', font=('Times New Roman',14), justification='left', expand_x=True)],
  [sg.Input(key='email')]
]

coluna_nome = [
  [sg.Text(f'Nome: ', font=('Times New Roman',14), justification='left', expand_x=True)],
  [sg.Input(key='nome'), sg.Button('Buscar')]
]

coluna_cep = [
[sg.Text(f'CEP: ', font=('Times New Roman',14), justification='left', expand_x=True)],
[sg.Input(key='cep'), sg.Button('Buscar')] 
]

coluna_logradouro = [
  [sg.Text('Logradouro: ')],
  [sg.Input(key='logradouro')]
]

coluna_numero = [
  [sg.Text('Número: ')],
  [sg.Input(key='numero')]
]

coluna_bairro = [
  [sg.Text('Bairro')],
  [sg.Input(key='bairro')]
]

coluna_estado = [
  [sg.Text('Estado')],
  [sg.Combo(estado, default_value='Escolha um estado', readonly=True, key='estadocombo')]
]

coluna_cidade = [
  [sg.Text('Cidade')],
  [sg.Combo(cidade, default_value="Escolha uma cidade", readonly=True, key='cidadecombo' )]
]

coluna_telefone = [
  [sg.Text('Telefone: ')],
  [sg.Input(key='telefone')]
]


layout = [
  [sg.Column(coluna_email, element_justification='left')],
  [sg.Column(coluna_nome, element_justification='left')],
  [sg.Column(coluna_cep, element_justification='left')],
  [sg.Column(coluna_logradouro, pad=(0,0), element_justification='left'), sg.Column(coluna_numero, pad=(20,0), element_justification='left')],
  [sg.Column(coluna_bairro, pad=(0,0), element_justification='left'), sg.Column(coluna_estado, pad=(0,0), element_justification='left'), sg.Column(coluna_cidade, pad=(20,0), element_justification='left')],
  [sg.Column(coluna_telefone, pad=(0,0), element_justification='left')],
  [sg.Button('Novo'), sg.Button('Salvar'), sg.Button('Cancelar'), sg.Button('Excluir'), sg.Button('Fechar')]
]

janela = sg.Window('Cadastro de clientes', layout)

while True:
  evento, valores = janela.read()

  if evento == sg.WIN_CLOSED or evento == "Fechar":
    break
  elif evento == 'Cancelar':
    janela['email'].update('')
    janela['nome'].update('')
    janela['cep'].update('')
    janela['logradouro'].update('')
    janela['numero'].update('')
    janela['bairro'].update('')
    janela['autorcombo'].update(value='Escolha o autor')
    janela['generocombo'].update(value='Escolha o gênero')
  elif evento == 'Buscar':
    if len(valores['isbn']) > 13:
      sg.popup(f'Você digitou mais números que o permitido!')
      janela['isbn'].update('')



janela.close()
