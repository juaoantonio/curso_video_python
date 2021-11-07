from time import sleep


def linha():
    print('=-=' * 15)


def contador(inicio, fim, passo):
    sequencia = 0
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
        if passo > 0:
            sequencia = list(range(inicio, fim + 1, passo))

        elif passo == 0:
            sequencia = list(range(inicio, fim + 1, 1))

        else:
            print(f'Passo {passo} inválido!')

    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim}, de {- passo} em {- passo}')
        if passo > 0:
            sequencia = list(range(inicio, fim - 1, - passo))

        elif passo < 0:
            sequencia = list(range(inicio, fim - 1, passo))

        else:
            sequencia = list(range(inicio, fim - 1, -1))

    for numero in sequencia:
        print(numero, end=' ')
        sleep(0.5)
    print('FIM')
    sleep(0.5)


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input(f'{"Ínicio: ":<8}'))
fim = int(input(f'{"Fim: ":<8}'))
passo = int(input(f'{"Passo: ":<8}'))
linha()
contador(inicio, fim, passo)
