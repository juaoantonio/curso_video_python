r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira: '))

if (r2 + r3) > r1 > (r2 - r3):
    if r1 == r2 == r3:
        tipo = 'EQUILÁTERO'

    elif r1 != r2 != r3 != r1:
        tipo = 'ESCALENO'

    else:
        tipo = 'ISÓCELES'

    print(f'Essas retas podem formar um triângulo {tipo}')
else:
    print('Infelizmente, essas retas não podem formar um triângulo')
