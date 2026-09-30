'''
Faça o programa referente a tela a seguir. Seu programa deve receber o gênero e a
altura de uma pessoa e deve calcular seu peso ideal. Programe também os botões
Limpar (que limpa o InputText e retorna o Radio ao valor padrão) e o botão Sair (que
fecha a aplicação).
Fórmulas:
Homens => Peso Ideal = altura * 72,7 - 58
Mulheres => Peso Ideal = altura * 62,1 – 44,7
'''
from tkinter import *
from tkinter import messagebox


def calculo():
  if opcaoSelecionada.get() == 'fem':
    fem = float(altura.get()) * 62.1 - 44.7
    resultado.set(fem)
  elif opcaoSelecionada.get() == 'mas':
    resultado.set(float(altura.get()) * 72.7 - 58)
    
def limpar():
  altura.set("")
  resultado.set("")
  opcaoSelecionada.set(value='fem')
  
def fechar():
  #este comando fecha a janela retirando da memoria 
  resposta = messagebox.askyesno("Confirmação", "Tem certeza?")
  if resposta:
    janela.destroy()


janela = Tk()

janela.title('Calculo de peso ideal')
janela.configure(background='#E6E6FA')
janela.geometry('400x350')


lblgenero = Label(janela, text='Selecione o gênero: ', background='#E6E6FA').place(x=40, y=50)
opcaoSelecionada = StringVar(value='fem')
fem = Radiobutton(janela, text="Feminino", variable=opcaoSelecionada, value="fem", background='#E6E6FA').place(x=40,y=80)
mas = Radiobutton(janela, text="Masculino", variable=opcaoSelecionada, value="mas", background='#E6E6FA').place(x=120,y=80)

lblaltura = Label(janela, text='Altura: ', background='#E6E6FA').place(x=40, y=120)
altura = StringVar(janela)
txtaltura = Entry(janela, width=20, textvariable=altura)
txtaltura.place(x=100, y=120)

lblResultado = Label(janela, text='Resultado: ', background='#E6E6FA').place(x=40, y=160)
resultado = StringVar(janela)
txtResultado = Label(janela, textvariable=resultado, background='#E6E6FA').place(x=100, y=160)


btnconverter = Button(janela, text='Calcular', width=8, command=calculo, background='#BA55D3').place(x=40, y=280)
btnlimpar = Button(janela, text='Limpar', width=8, command=limpar, background='#BA55D3').place(x=140, y=280)
btnfechar = Button(janela, text='Fechar', width=8, command=fechar, background='#BA55D3').place(x=240, y=280)

#este comando mantém a janela aberta 
janela.mainloop()