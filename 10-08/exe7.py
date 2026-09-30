'''
7) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma sequência em
P.A. contendo 10 valores.
'''

a = int(input(f'Informe um valor: '))
r = int(input(f'Informe a razão: '))

for i in range(10):
  if i == 0:
    print(a)
  else:
    a += r
    print(a)
