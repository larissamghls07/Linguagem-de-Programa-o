


menu_def = [
  ['Cadastro', ['Autores', 'Clientes', 'Gênero', 'Livros', '---', 'Sair']],
  ['Operações', ['Consulta', 'Empréstimo', 'Venda']],
  ['Relatórios', ['Clientes', 'Livros Emprestados', 'Preços de livros']],
  ['Ajuda', ['Sobre...']]
]


janela = sg.Window('Menu principal', layout)

while True:
  evento, valores = janela.read()

  if evento == sg.WIN_CLOSED or evento == "Fechar":
    break
  elif evento == ''