print('Olá, sou um programa que serve para ajudar a calcular médias de alunos.')
print('Digite as duas notas as quais você quer a média')
n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda? '))
media = round((n1+n2)/2, 1)
print(f'A média dessas notas é: {media}')
