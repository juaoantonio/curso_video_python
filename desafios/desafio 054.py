from datetime import datetime
ano_atual = datetime.now().year

maiores_de_idade = 0
menores_de_idade = 0

for pessoa in range(1, 7):
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    if ano_atual - nascimento >= 18:
        maiores_de_idade += 1

    else:
        menores_de_idade += 1

print(f'No total, temos {maiores_de_idade} pessoas maiores de idade')
if menores_de_idade > 0:
    print(f'E {menores_de_idade} menores de idade')
