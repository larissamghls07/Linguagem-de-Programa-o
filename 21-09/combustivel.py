'''
Faça o programa referente a tela a seguir. Seu programa deve receber os preços da
gasolina e do etanol e avaliar se é melhor abastecer com Etanol, Gasolina ou com
Etanol ou Gasolina (tanto faz). Para isso considere que o Etanol rende apenas 70% da
gasolina. Programe também os botões Limpar (que retorna os InputText e o Text e
para o estado original) e o botão sair (que fecha a aplicação).
'''
#já vem no pacote original do python
from tkinter import *
from tkinter import messagebox


def conversao():
  if etanol.get() != '' and gasolina.get() != '':
    if float(etanol.get()) < (0.7*float(gasolina.get())):
      resultado.set("Abasteça com etanol!")
    elif float(etanol.get()) == (0.7*float(gasolina.get())):
      resultado.set("Tanto faz.")
    else:
      resultado.set("Abasteça com gasolina!")
  elif etanol.get() == '':
    messagebox.showwarning("Atenção", "O valor de etanol é obrigatório!")
  elif gasolina.get() == '':
    messagebox.showwarning("Atenção", "O valor da gasolina é obrigatória!")
  else:
    messagebox.showwarning("Atenção", "Os valores de gasolina e etanol são obrigatórios!")
def limpar():
  gasolina.set("")
  etanol.set("")
  resultado.set("")

def fechar():
  #este comando fecha a janela retirando da memoria 
  resposta = messagebox.askyesno("Confirmação", "Tem certeza?")
  if resposta:
    janela.destroy()


#este comando cria uma instância de janela nessa variável
janela = Tk()
#define um título para a janela
janela.title('Conversor de combustível')
#define as dimensões 
janela.geometry("400x350") #larguraXaltura
#o ponto 0.0 começa do lado superior esquerdo

lblgasolina = Label(janela, text='Preço da gasolina: ').place(x=40, y=40)
gasolina = StringVar(janela) #uma palavra reservada que define como string 
txtgasolina = Entry(janela, width=20, textvariable=gasolina) #Esse componente está ligado à variável definina anteriormente
txtgasolina.place(x=160, y=40)


lbletanol = Label(janela, text='Preço do etanol: ').place(x=40, y=80)
etanol = StringVar(janela)
txtetanol = Entry(janela, width=20, textvariable=etanol)
txtetanol.place(x=160, y=80)

lblResultado = Label(janela, text='Resultado: ').place(x=40, y=160)
resultado = StringVar(janela)
txtResultado = Label(janela, textvariable=resultado).place(x=100, y=160)


btnconverter = Button(janela, text='Converter', width=8, command=conversao).place(x=40, y=280)
btnlimpar = Button(janela, text='Limpar', width=8, command=limpar).place(x=140, y=280)
btnfechar = Button(janela, text='Fechar', width=8, command=fechar).place(x=240, y=280)

#este comando mantém a janela aberta 
janela.mainloop()