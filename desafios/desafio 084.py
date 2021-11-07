pessoas = []
pessoa = []
maior_peso = menor_peso = 0

while True:
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        menor_peso = pessoa[1]
        maior_peso = pessoa[1]

    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]

        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]

    pessoas.append(pessoa[:])

    pessoa.clear()

    continuar = ''

    while continuar != 's' and continuar != 'n':
        continuar = input('Gostaria de continuar? [S/N] ')

        str(continuar).strip().lower()
        if continuar != 's' and continuar != 'n':
            print('Não entendi, tente novamente!')

    if continuar == 's':
        print()
        pass
    elif continuar == 'n':
        print()
        break

print(f'Um total de {len(pessoas)} pessoas foram cadastradas.')

print(f'O maior peso foi {maior_peso:.1f} Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')

print(f'\nO maior peso foi {menor_peso:.1f} Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')
