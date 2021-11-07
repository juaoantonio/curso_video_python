num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1

print()
print('Aqui está seu resultado')

while num != 0:
    print(f'{num} ', end='')
    if num > 1:
        fatorial *= num
        num = num - 1
        print('x ', end='')

    else:
        num = num - 1
        print('= ', end='')

print(fatorial)
