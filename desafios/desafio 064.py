contador = num = soma = 0

while num != 999:
    num = int(input('Digite um valor: [999 para parar] '))
    if num != 999:
        soma += num
        contador += 1

print(f'Você digitou o total de {contador} números e a soma entre eles é igual a {soma}')