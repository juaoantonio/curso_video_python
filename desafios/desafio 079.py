numeros = []

while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
    else:
        print('Esse número já existe na lista, não irei adicionar')

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

print(f'Sua lista é {numeros.sort()}')
