'''
3) Desenvolver um algoritmo que leia 20 números inteiros e calcule e escreva a média aritmética
dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o
percentual de valores negativos e positivos.
'''

numeros = []
media, soma, qtdpositivo, qtdnegativo = 0, 0, 0, 0

for i in range(20):
  num = float(input(f'Informe um número: '))
  soma += num
  if num < 0:
    qtdnegativo += 1
  if num > 0:
    qtdpositivo += 1

media = soma / 20

print(f'A média: {media}')
print(f'A quantidade de positivos: {qtdpositivo} e o percentual é de {(qtdpositivo/20) * 100}%.')
print(f'A quantidade de negativos: {qtdnegativo} e o percentual é de {(qtdnegativo/20) * 100}%.')