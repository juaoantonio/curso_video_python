num = int(input('Digite um número: '))

divisores = []

for c in range(1, num + 1):
    if num % c == 0:
        divisores.append(c)

if len(divisores) != 2:
    print(f'{num} não é primo, pois possui {len(divisores)} divisores:')
    for divisor in divisores:
        print(divisor, end=' ')

else:
    print(f'{num} é primo, pois possui somente 2 divisores.')