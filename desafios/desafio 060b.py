num = int(input('Digite um número para que eu possa calcular seu fatorial: '))
resultado = 1

for c in range(num, 0, -1):
    print(f'{c}', end='')
    print(' x' if c > 1 else ' =', end=' ')
    resultado *= c
print(resultado)
