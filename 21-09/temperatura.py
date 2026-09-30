#já vem no pacote original do python
from tkinter import *

#cria funções para os botoes antes da parte gráfica 

def converter():
  print('Apertei no botão de converter')
  f = (float(celsius.get()) * 1.8) + 32
  fahrenheit.set(f)
  k = float(celsius.get()) + 273
  kelvin.set(k)
  

def limpar():
  #pegar as variaveis que estavam armazenando e limpar 
  #set significa colocar algo em algum lugar 
  celsius.set("")
  fahrenheit.set("")
  kelvin.set("")

def fechar():
  #este comando fecha a janela retirando da memoria 
  janela.destroy()


#este comando cria uma instância de janela nessa variável
janela = Tk()
#define um título para a janela
janela.title('Conversor de temperatura')
#define as dimensões 
janela.geometry("400x350") #larguraXaltura
#o ponto 0.0 começa do lado superior esquerdo

lblcelsius = Label(janela, text='Celsius: ').place(x=40, y=40)
celsius = StringVar(janela) #uma palavra reservada que define como string 
txtcelsius = Entry(janela, width=20, textvariable=celsius) #Esse componente está ligado à variável definina anteriormente
txtcelsius.place(x=120, y=40)


#Bloco do Fahrenheit 
lblfahrenheit = Label(janela, text='Fahrenheit: ').place(x=40, y=80)
fahrenheit = StringVar(janela)
txtfahrenheit = Entry(janela, width=20, textvariable=fahrenheit)
txtfahrenheit.place(x=120, y=80)

#Bloco do Kelvin 

lblkelvin = Label(janela, text='Kelvin: ').place(x=40, y=120)
kelvin = StringVar(janela)
txtkelvin = Entry(janela, width=20, textvariable=kelvin)
txtkelvin.place(x=120, y=120)


btnconverter = Button(janela, text='Converter', width=8, command=converter).place(x=40, y=280)
btnlimpar = Button(janela, text='Limpar', width=8, command=limpar).place(x=140, y=280)
btnfechar = Button(janela, text='Fechar', width=8, command=fechar).place(x=240, y=280)

#este comando mantém a janela aberta 
janela.mainloop()