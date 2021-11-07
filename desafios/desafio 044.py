print('LOJAS BARBOSA'.center(50, '='))
print()

preco = float(input('Qual o valor do produto? R$'))
print()

forma_de_pagamento = """Escolha a forma de pagamento:
[1] À vista, em dinheiro ou cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Até 2x no cartão: preço original
[4] 3x ou mais no cartão: 20% de juros\n"""

print(forma_de_pagamento)
opcao = int(input('Qual sua opção? '))

valor_final = 0

if opcao == 1:
    valor_final = preco - (preco * 10/100)

elif opcao == 2:
    valor_final = preco - (preco * 5/100)

elif opcao == 3:
    valor_final = preco

elif opcao == 4:
    valor_final = preco + (preco * 20/100)

else:
    print('Insira um valor válido!!!')

print(f'O valor final do seu produto é R${valor_final:.2f}')
