'''
4) Escrever um algoritmo que leia a idade de 50 pessoas e conte quantos delas estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
'''

um, dois, tres, quatro = 0, 0, 0, 0 

for i in range(10):
  idade = int(input(f'Informe a sua idade: '))
  if idade <=26:
    um += 1
  elif idade <=50:
    dois += 1
  elif idade <=75:
    tres += 1
  else:
    quatro += 1

print(f'A quantidade de pessoas no intervalo, segue a tabela abaixo:\n[0 - 25]: {um};\n[26 - 50]: {dois};\n[51 - 75]: {tres};\n[76 - 100]: {quatro}.')