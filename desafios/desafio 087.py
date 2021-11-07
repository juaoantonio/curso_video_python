matriz = [[], [], []]
pares = []
terceira_coluna = []
segunda_linha = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'Digite um número para a posição [{linha}, {coluna}]: '))
        matriz[linha].append(numero)
        if numero % 2 == 0:
            pares.append(numero)

        if coluna == 2:
            terceira_coluna.append(numero)

        if linha == 1:
            segunda_linha.append(numero)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end=' | ')
    print()

print(f'\nA soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {sum(terceira_coluna)}')
print(f'O maior valor da segunda linha é {max(segunda_linha)}')
