num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo: '))
num3 = float(input('Digite o terceiro: '))

# Para descobrir qual o maior:
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f'O maior número é {maior}')

# Para descobrir qual o menor:
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'E o menor número é {menor}')
