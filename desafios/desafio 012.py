# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Qual o valor original do produto? '))
d = float(input('Qual o valor do desconto que está aplicado? '))

print(f'Com {d}% de desconto, o preço anterior passa a valer R${p - p * (d / 100):.2f}')
