from time import sleep


def maior(arg=0, *numeros):
    print('=-=' * 15)
    print('Analisando os valores passados...')
    lista = [numeros]
    if len(numeros) > 0:
        maior_numero = max(lista)[0]
        for num in numeros:
            print(num, end=' ')
            sleep(0.5)
        print(f'\nForam informados {len(numeros)} numeros')
        print(f'O maior valor informado foi {maior_numero}')
        sleep(1)
    else:
        print(f'Foi informados {arg} numeros')
        print(f'Não há maior valor!')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
