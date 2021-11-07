# Faça um programa que leia um número inteiro qualquer e mostre sua tabuada na tela
n = int(input('Digite um número inteiro para que eu possa te mostrar a tabuada dele: '))

print(f'Aqui está a tabuada de {n}:')
for m in range(1, 11):
    print(f'{n} x {m} = {n*m}')

