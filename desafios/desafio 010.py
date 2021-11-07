# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
print('Olá! Sou um programa que vai ajudar você a saber ', end='')
print('quantos dólares você pode comprar com seu saldo atual de reais.')

r = float(input('Diga qual seu saldo de reais: R$'))
d = r / 5.40
print(f'Você pode comprar aproximadamente U${d:.2f}')
