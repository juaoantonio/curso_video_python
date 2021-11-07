from random import randint


def sorteia(lst):
    for cont in range(0, 5):
        lst.append(randint(1, 10))
    print('Os numeros sorteados foram:')
    for num in lst:
        print(num, end=' ')
    print()


def somaPar(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lst}, o resultado é o valor {soma}')


numeros = list()
sorteia(numeros)
print()
somaPar(numeros)

