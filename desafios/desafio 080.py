numeros = []

for cont in range(0, 5):
    numero = int(input('Digite um valor: '))
    if cont == 0 or numero >= numeros[-1]:
        numeros.append(numero)
        print('Adicionando o valor ao final da lista...')

    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                print(f'Adicionando o número na posição {pos}')
                break
            pos += 1
print(numeros)