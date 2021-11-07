from statistics import mean
from time import sleep
alunos = []
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    alunos.append([nome, [nota1, nota2]])

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print('-=' * 30)

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for cont in range(0, len(alunos)):
    print(f'{cont:<4}{alunos[cont][0]:<10}{mean(alunos[cont][1]):>8.1f}')
print('-' * 26)

while True:
    selecao = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if 0 <= selecao <= len(alunos) - 1:
        print(f'Notas de {alunos[selecao][0]}: {alunos[selecao][1]}')

    elif selecao == 999:
        break

    else:
        print('Aluno não existente!')

print('Finalizando', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(1)
print('\nVolte sempre!')
sleep(1)
