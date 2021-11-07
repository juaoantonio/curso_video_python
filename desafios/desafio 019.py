import random
a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo? ')
a3 = input('Qual o nome do terceiro? ')
a4 = input('Qual o nome do quarto? ')
lista = [a1, a2, a3, a4]
sort = random.choice(lista)
print(f'O nome do aluno(a) escolhido foi: {sort}')