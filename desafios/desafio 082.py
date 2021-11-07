valores = []
impares = []
pares = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0 and valor != 0:
        pares.append(valor)
    else:
        impares.append(valor)

    continuar = input('Quer continuar [S/N] ')
    str(continuar)

    while continuar != 's' and  continuar != 'n':
        print('Não entendi. Tente novamente!')
        continuar = input('Quer continuar [S/N] ')

    if continuar == 'n':
        break

print(f'\nTodos os valores informados: {valores}')
print(f'Todos os valores pares digitados: {pares}')
print(f'Todos os valores ímpares digitados: {impares}')
