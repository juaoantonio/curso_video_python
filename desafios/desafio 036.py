print('-' * 50)
print('APROVAÇÃO DE EMPRÉSTIMO'.center(50, '-'))
print('-' * 50)

casa = float(input('Qual o valor da casa que você quer comprar? R$'))
salario = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você irá pagar? '))

prestacao = casa / (anos * 12)

print('-' * 50)

if prestacao <= salario * 0.3:
    print(f'\033[1;32mSeu empréstimo foi aprovado!\033[m Sua prestação mensal é de R${prestacao:.2f}.')
else:
    print(f'\033[1;31mSeu empréstimo não foi aprovado\033[m, pois a prestação de R${prestacao:.2f} execedeu o limite de 30%', end='')
    print(f' do seu salário de R${salario}')
