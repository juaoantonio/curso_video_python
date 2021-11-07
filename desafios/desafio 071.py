# Cabeçalho
print('-' * 50)
print('Banco Barbosa'.center(50))
print('-' * 50)

# O saque só poderá ser realizado com nota de 50, 20, 10, 5 e 1 reais
reais = int(input('Qual o valor a ser sacado? R$'))

# Variáveis
nota50 = nota20 = nota10 = nota5 = nota1 = 0

# Listas
notas = [nota50, nota20, nota10, nota5, nota1]
valores = [50, 20, 10, 5, 1]

# Iterações
for nota, valor in zip(notas, valores):
    while reais - valor >= 0:
        nota += 1
        reais -= valor

    if nota != 0:
        print(f'Total de {nota} cédulas de R${valor}.00 ')

# Final do programa
print('-' * 50)
print('Volte sempre!')
