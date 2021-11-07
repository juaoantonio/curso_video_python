# Variáveis

maiores_de_idade = 0
homens = 0
mulheres_menos_de_20 = 0

# Repetição dos inputs

while True:
    # Cabeçalho do programa

    print('-' * 50)
    print('CADASTRE UMA PESSOA'.center(50))
    print('-' * 50)

    # Inputs de idade e sexo e as condições para cada caso

    idade = int(input('Idade: '))
    if idade >= 18:
        maiores_de_idade += 1

    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo[0] == 'M':
        homens += 1

    elif sexo[0] == 'F' and idade >= 20:
        mulheres_menos_de_20 += 1

    print('-' * 50)

    # Pergunta para usuário se ele quer continuar no programa

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        print('Não entendi. Digite algo válido!')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    if continuar == 'N':
        break

# Resultado final

print()
print(f'''Resultados da análise:
Total de pessoas com mais de 18 anos: {maiores_de_idade}
Total de homens cadastrados: {homens}
Total de mulheres com mais de 20 anos: {mulheres_menos_de_20}''')
