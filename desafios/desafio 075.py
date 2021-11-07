numeros = tuple(int(input('Digite um valor: ')) for c in range(1, 5))
pares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1

print(f'O numero 9 apareceu {numeros.count(9)} vezes')
print(f'A primeira aparição do número 3 foi na {numeros.index(3) + 1}ª posição')
print(f'Temos {pares} números pares')
