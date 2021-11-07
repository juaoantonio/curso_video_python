def fatorial(num: int, show: bool = False):
    """
    -> Calcula o fatorial de um número maior que zero
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não o cálculo
    :return: O valor do fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c != 1:
                print(' x ', end='')
            else:
                print(' = ', end=' ')
        f *= c

    return f


# Programa principal
n = int(input('Digite um valor: '))
print(fatorial(n, show=True))
help(fatorial)
