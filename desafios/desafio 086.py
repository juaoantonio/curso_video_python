matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'Digite um número para a posição [{linha}, {coluna}]: '))
        matriz[linha].append(numero)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end=' | ')
    print()
