from statistics import mean
pessoas = []

while True:
    nome = str(input('Nome: ')).strip().title()

    sexo = str(input('Sexo: [M/F] ')).strip().lower()
    while sexo != 'm' and sexo != 'f':
        print('Erro: por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).strip().lower()

    idade = int(input('Idade: '))

    pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})

    continuar = str(input('\nDeseja continuar? [S/N] ')).strip().lower()
    while continuar != 's' and continuar != 'n':
        print('Erro: por favor, digite apenas s ou n.')
        continuar = str(input('\nDeseja continuar? [S/N] ')).strip().lower()

    if continuar == 'n':
        break

print(f'A) Ao todo, temos {len(pessoas)} pessoas cadastradas.')

idades = [pessoas[cont]['idade'] for cont in range(0, len(pessoas))]
media_idades = mean(idades)
print(f'B) A média das idades é de {media_idades:.2f}')

print(f'C) As mulheres cadastradas foram', end=' ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'f':
        print(f"[{pessoa['nome']}]", end= ' ')

print('\nD) Lista das pessoas que estão acima da média de idade:')
for pessoa in pessoas:
    if pessoa['idade'] > media_idades:
        print(f'    Nome = {pessoa["nome"]}; Sexo = {pessoa["sexo"].title()}; Idade = {pessoa["idade"]}')

print()
print('<<< ENCERRADO >>>'.center(50))
