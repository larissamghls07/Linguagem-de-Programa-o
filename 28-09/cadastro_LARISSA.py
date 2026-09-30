from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests


class Cliente:
    def __init__(self, email="", nome="", estado_civil="", ocupacao="", genero="", 
                 cep="", endereco="", numero="", bairro="", estado="", cidade="", telefone=""):
        self._email = email
        self._nome = nome
        self._estado_civil = estado_civil
        self._ocupacao = ocupacao
        self._genero = genero
        self._cep = cep
        self._endereco = endereco
        self._numero = numero
        self._bairro = bairro
        self._estado = estado
        self._cidade = cidade
        self._telefone = telefone

    # --- Getters e Setters ---
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def estado_civil(self):
        return self._estado_civil
    @estado_civil.setter
    def estado_civil(self, valor):
        self._estado_civil = valor

    @property
    def ocupacao(self):
        return self._ocupacao
    @ocupacao.setter
    def ocupacao(self, valor):
        self._ocupacao = valor

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def cep(self):
        return self._cep
    @cep.setter
    def cep(self, valor):
        self._cep = valor

    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def bairro(self):
        return self._bairro
    @bairro.setter
    def bairro(self, valor):
        self._bairro = valor

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self, valor):
        self._cidade = valor

    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    # --- Método __str__ para impressão ---
    def __str__(self):
        return (
            f"--- Cliente Cadastrado ---\n"
            f"Email: {self._email}\n"
            f"Nome: {self._nome}\n"
            f"Estado Civil: {self._estado_civil}\n"
            f"Ocupação: {self._ocupacao}\n"
            f"Gênero: {self._genero}\n"
            f"CEP: {self._cep}\n"
            f"Endereço: {self._endereco}\n"
            f"Número: {self._numero}\n"
            f"Bairro: {self._bairro}\n"
            f"Estado: {self._estado}\n"
            f"Cidade: {self._cidade}\n"
            f"Telefone: {self._telefone}"
        )

generos = ['Mulher', 'Homem', 'Não-Binário', 'Transgênero', 'Agênero', 'Gênero Fluido', 'Travesti', 'Bigênero', 'Pangênero','Demigênero','Andrógine']

estados = {
  'Acre': 'AC', 'Alagoas': 'AL', 'Amapá': 'AP', 'Amazonas': 'AM', 'Bahia': 'BA',
  'Ceará': 'CE', 'Distrito Federal': 'DF', 'Espírito Santo': 'ES', 'Goiás': 'GO',
  'Maranhão': 'MA', 'Mato Grosso': 'MT', 'Mato Grosso do Sul': 'MS', 'Minas Gerais': 'MG', 'Pará': 'PA', 'Paraíba': 'PB', 'Paraná': 'PR', 'Pernambuco': 'PE', 'Piauí': 'PI',
  'Rio de Janeiro': 'RJ', 'Rio Grande do Norte': 'RN', 'Rio Grande do Sul': 'RS',
  'Rondônia': 'RO', 'Roraima': 'RR', 'Santa Catarina': 'SC', 'São Paulo': 'SP',
  'Sergipe': 'SE', 'Tocantins': 'TO'
}


def carregar_cidades():
  if estado.get() == '':
    messagebox.showwarning("Atenção", "Selecione um estado!")
  else:
    #tive que pear isso com IA, não entendi muito bem o uso dessa API
    # API do IBGE: devolve os municípios do estado selecionado
        sigla = estados[estado.get()]
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + sigla + '/municipios?orderBy=nome'
        resposta = requests.get(url)
        cidades = []
        for c in resposta.json():
          cidades.append(c['nome'])
        cmbcidade['values'] = cidades
        cidade.set("")



def buscar():
  # deixa só os números do CEP
  #o join permite que junte vários caracteres numa única strin g
  #o cep.get() extrai o texto que o usuarioo vai diitar, a série de comandos diz o seuinte> filtra o texto e deixa apenas os caracteres que sao numéricos, mesmo que a pessoa coloque trqaços ou outrs símbolos, apenas os números serão considerados. 
  numeros = ''.join(c for c in cep.get() if c.isdigit())
  if len(numeros) != 8:
    messagebox.showwarning("Atenção", "Digite um CEP válido com 8 números!")
    return
  else:
    # API do ViaCEP: devolve o endereço do CEP
    resposta = requests.get(f'https://viacep.com.br/ws/{numeros}/json/', timeout=10)
    dados = resposta.json()
    if 'erro' in dados:
      messagebox.showwarning("Atenção", "CEP não encontrado!")
      return
    endereco.set(dados['logradouro'])
    bairro.set(dados['bairro'])
    # descobre o nome do estado a partir da sigla devolvida
    for nome, sigla in estados.items():
      if sigla == dados['uf']:
        estado.set(nome)
        carregar_cidades()
        cidade.set(dados['localidade'])
        break


def limpar():
  email.set("")
  nome.set("")
  estadocivil.set("")
  estuda.set(0)
  trabalha.set(0)
  genero.set("")
  cep.set("")
  endereco.set("")
  numero.set("")
  bairro.set("")
  estado.set("")
  cidade.set("")
  cmbcidade['values'] = []
  telefone.set("")


def cadastrar():
    # Validação de campos obrigatórios
    if email.get() == '':
        messagebox.showwarning("Atenção", "O campo Email é obrigatório!")
    elif nome.get() == '':
        messagebox.showwarning("Atenção", "O campo Nome é obrigatório!")
    elif estadocivil.get() == '':
        messagebox.showwarning("Atenção", "O campo Estado Civil é obrigatório!")
    elif telefone.get() == '':
        messagebox.showwarning("Atenção", "O campo Telefone é obrigatório!")
    else:
        # Montar lista de ocupações
        lista_ocupacao = []
        if estuda.get() == 1:
            lista_ocupacao.append('Estuda')
        if trabalha.get() == 1:
            lista_ocupacao.append('Trabalha')
        str_ocupacao = ', '.join(lista_ocupacao) if lista_ocupacao else 'Nenhuma'

        # Instanciar a classe Cliente
        novo_cliente = Cliente()

        # Atribuir os valores através dos setters
        novo_cliente.email = email.get()
        novo_cliente.nome = nome.get()
        novo_cliente.estado_civil = estadocivil.get()
        novo_cliente.ocupacao = str_ocupacao
        novo_cliente.genero = genero.get()
        novo_cliente.cep = cep.get()
        novo_cliente.endereco = endereco.get()
        novo_cliente.numero = numero.get()
        novo_cliente.bairro = bairro.get()
        novo_cliente.estado = estado.get()
        novo_cliente.cidade = cidade.get()
        novo_cliente.telefone = telefone.get()

        # Imprimir no terminal o conteúdo do objeto (utilizando o __str__)
        print(novo_cliente)

        messagebox.showinfo("Sucesso", "Registro gravado com sucesso!")
        limpar()

def fechar():
  resposta = messagebox.askyesno("Verificação", "Deseja sair realmente?")
  if resposta:
    janela.destroy()


janela = Tk()
janela.title('Cadastro de Clientes | LARISSA')
janela.geometry("780x270") 

lblemail = Label(janela, text='Email*: ').place(x=20, y=20)
email = StringVar(janela)
txtemail = Entry(janela, width=80, textvariable=email)
txtemail.place(x=110, y=20)


lblnome = Label(janela, text='Nome*: ').place(x=20, y=55)
nome = StringVar(janela)
txtnome = Entry(janela, width=80, textvariable=nome)
txtnome.place(x=110, y=55)


lblestadocivil = Label(janela, text='Estado Civil*: ').place(x=20, y=90)
estadocivil = StringVar(janela)
rdsolteiro = Radiobutton(janela, text='Solteiro', variable=estadocivil, value='Solteiro').place(x=110, y=90)
rdcasado = Radiobutton(janela, text='Casado', variable=estadocivil, value='Casado').place(x=190, y=90)

lblocupacao = Label(janela, text='Ocupação: ').place(x=290, y=90)
estuda = IntVar(janela)
trabalha = IntVar(janela)
chkestuda = Checkbutton(janela, text='Estuda', variable=estuda).place(x=360, y=90)
chktrabalha = Checkbutton(janela, text='Trabalha', variable=trabalha).place(x=430, y=90)


lblgenero = Label(janela, text='Gênero: ').place(x=530, y=90)
genero = StringVar(janela)
cmbgenero = ttk.Combobox(janela, width=17, textvariable=genero, values=generos, state='readonly')
cmbgenero.place(x=590, y=90)


lblcep = Label(janela, text='CEP: ').place(x=20, y=125)
cep = StringVar(janela)
txtcep = Entry(janela, width=12, textvariable=cep)
txtcep.place(x=110, y=125)
btnbuscar = Button(janela, text='Buscar', width=6, command=buscar).place(x=210, y=122)


lblendereco = Label(janela, text='Endereço: ').place(x=290, y=125)
endereco = StringVar(janela)
txtendereco = Entry(janela, width=32, textvariable=endereco)
txtendereco.place(x=360, y=125)


lblnumero = Label(janela, text='Número: ').place(x=610, y=125)
numero = StringVar(janela)
txtnumero = Entry(janela, width=8, textvariable=numero)
txtnumero.place(x=670, y=125)


lblbairro = Label(janela, text='Bairro: ').place(x=20, y=160)
bairro = StringVar(janela)
txtbairro = Entry(janela, width=25, textvariable=bairro)
txtbairro.place(x=110, y=160)


lblestado = Label(janela, text='Estado: ').place(x=290, y=160)
estado = StringVar(janela)
cmbestado = ttk.Combobox(janela, width=18, textvariable=estado, values=list(estados.keys()), state='readonly')

#esse .keys é um método do python que conseue pear as chaves existentes no dicionario feito la pra cima, seleciona o que está depois do dois pontos entre as aspas simples usadas no meu caso. Quando usa o list() e dentro o nome do dicionario, vai mostrar como se fosse assim: Saída: ['SP', 'RJ', 'MG']
cmbestado.place(x=350, y=160)
# quando o usuário escolhe um estado, carrega as cidades dele
cmbestado.bind('<<ComboboxSelected>>', carregar_cidades)

lblcidade = Label(janela, text='Cidade: ').place(x=510, y=160)
cidade = StringVar(janela)
cmbcidade = ttk.Combobox(janela, width=25, textvariable=cidade, state='readonly')
cmbcidade.place(x=570, y=160)


lbltelefone = Label(janela, text='Telefone*: ').place(x=20, y=195)
telefone = StringVar(janela)
txttelefone = Entry(janela, width=25, textvariable=telefone)
txttelefone.place(x=110, y=195)


btncadastrar = Button(janela, text='Cadastrar', width=8, command=cadastrar).place(x=20, y=230)
btnsair = Button(janela, text='Sair', width=8, command=fechar).place(x=120, y=230)

janela.mainloop()