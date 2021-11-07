nome = str(input('Digite seu nome completo: ')).strip().title()
dividido = nome.split()

print(f'Prazer em te conhecer, {dividido[0]}')
print(f'Seu primeiro nome é {dividido[0].title()}\nE seu último nome é {dividido[-1]}')
print(';)')
# O '-1' é necessário para ficar dentro do range do fatiamento, já que o len() começa a contar a partir de 1
# enquanto o fatiamento conta os elementos da lista gerada pelo split a partir do 0
