# Lendo o nome, idade e sexo de 4 pessoas:

idades = []
homem_mais_velho = 0
mulheres_menores_de_idade = 0
maior_idade = 0

for c in range(1, 5):
    print(f' {c}ª PESSOA '.center(50, '='))
    nome = str(input('Nome: ')).strip().title()

    idade = int(input('Idade: '))
    idades.append(idade)

    sexo = str(input('Sexo [M/F]: ')).lower().strip()

    if sexo == 'm':
        if idade > maior_idade:
            maior_idade = idade
            homem_mais_velho = nome

    elif sexo == 'f':
        if idade < 20:
            mulheres_menores_de_idade += 1

media_idades = sum(idades) / len(idades)

print(f'A média de idade do grupo é: {media_idades}')
if homem_mais_velho != 0:
    print(f'O nome do homem mais velho é {homem_mais_velho}')
else:
    print('Não foi encontrado nenhum homem')
print(f'E foi identificado um total de {mulheres_menores_de_idade} mulheres com menos de 20 anos')
