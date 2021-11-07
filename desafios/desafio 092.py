from datetime import date
pessoa = dict()
data_atual = date.today().year

nome = str(input('Nome: ')).strip().title()
pessoa['nome'] = nome

idade = data_atual - int(input('Ano de nascimento: '))
pessoa['idade'] = idade

ctps = int(input('Carteira de trabalho (0 "não tenho"): '))
if ctps != 0:
    pessoa['ctps'] = ctps

    contratacao = int(input('Ano de contratação: '))
    pessoa['contratação'] = contratacao

    salario = int(input('Salário: R$'))
    pessoa['salário'] = salario

    aposentadoria = idade + ((contratacao + 35) - data_atual)
    pessoa['aposentadoria'] = aposentadoria

for k, v in pessoa.items():
    print(f'   - {k.title()} é igual a {v}.')
if ctps == 0:
    print('   - Sem carteira de trabalho.')