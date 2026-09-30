'''
2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
mostrar:
• A menor altura do grupo;
• A maior altura do grupo;
'''

'''
Resolução do professor 
for i in range(15):
  altura = float(input('Digite uma altura: '))
  if i == 0 or altura>maior:
    maior = altura
  if i == 0 or altura<menor:
    menor = altura
'''

menor = float('inf')
maior, altura = 0, 0

alturas = []

for i in range(15):
  alturas.append(float(input('Informe a sua altura: ')))
  if alturas[i] < menor:
    menor = alturas[i]
  if alturas[i] > maior:
    maior = alturas[i]

print(f'Maior: {maior}\nMenor: {menor}.')