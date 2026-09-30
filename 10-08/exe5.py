'''
5) Faça um algoritmo estruturado que leia um número inteiro n e em seguida leia n números
inteiros. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média
geral dos números lidos.
'''
par, impar, mediapar, soma, mediaimpar, media, somapar, somaimpar = 0, 0, 0, 0, 0, 0, 0, 0

num = int(input(f'Informe um número: '))

for i in range(num):
  numero = int(input(f'Infome um número: '))
  if (numero%2) == 0:
    par += 1
    somapar += numero
    soma += numero
  else:
    impar += 1
    somaimpar += numero
    soma += numero


print(f'A quantidade de número pares: {par}.')
print(f'A média de números pares: {somapar/par}.')
print(f'A quantidade número ímpar: {impar}.')
print(f'A média de números impares: {somaimpar/impar}.')
print(f'A média geral: {soma/num}.')