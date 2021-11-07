# Cabeçalho do programa
print('-' * 50)
print('Lojas Barbosa'.center(50))
print('-' * 50)

# Variáveis
soma = 0
mais_de_mil = 0
menor = 0
contador = 0
mais_barato = ''

# Repetição dos inputs
while True:
    nome_produto = str(input('Nome do produto: ')).strip().lower()

    valor_produto = float(input('Valor do produto: R$'))
    contador += 1
    soma += valor_produto

    if contador == 1 or valor_produto < menor:
        menor = valor_produto
        mais_barato = nome_produto

    if valor_produto >= 1000:
        mais_de_mil += 1

    # Pergunta se quer continuar
    continuar = ''
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()

    if continuar == 'n':
        break

    print()

# Fim do programa
print()
print('FIM DO PROGRAMA'. center(50, '-'))
print()

print(f'''O valor total da compra foi: {soma:.2f}
Total de produtos que custaram mais de R$1000.00: {mais_de_mil}
O produto mais barato foi {mais_barato}, que custou {menor:.2f}''')
