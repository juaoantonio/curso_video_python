while True:
    num = int(input('Quer ver a tabuada de qual valor? (0 para parar) '))

    if num == 0:
        print('Programa encerrado!')
        break

    print('-' * 50)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 50)
