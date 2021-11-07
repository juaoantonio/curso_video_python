valores = []
for cont in range(1, 6):
    valores.append(int(input(f'Digite um valor inteiro para a posição {cont}: ')))

print(f'Você digitou os valores {valores}')
minimo = min(valores)
maximo = max(valores)

print('=' * 50)
print(f'O menor valor digitado foi {minimo}, nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == minimo:
        print(pos + 1, end='... ')

print()
print(f'O maior valor digitado foi {maximo}, nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == maximo:
        print(pos + 1, end='... ')
