soma = cont = 0
while True:
    n = int(input('Digite um valor (0 para parar): '))
    if n == 0:
        break
    soma += n
    cont += 1

print(f'O total de números digitados foi {cont}')
print(f'A soma entre esses números foi {soma}')
