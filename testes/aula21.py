def par(n=0):
    if n % 2 == 0:
        return True

    else:
        return False


n = int(input('Digite um valor: '))
if par(n):
    if n == 0:
        print('Valor neutro!')

    else:
        print('É par!')

else:
    print('É ímpar!')