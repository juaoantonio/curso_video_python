from datetime import date

nascimento = int(input('Qual ano você nasceu? '))

idade = date.today().year - nascimento

print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('Classificação: MIRÍM')

elif idade <= 14:
    print('Classificação: INFANTIL')

elif idade <= 19:
    print('Classsificação: JÚNIOR')

elif idade <= 25:
    print('Classificação: SÊNIOR')

elif idade > 25:
    print('Classificação: MASTER')
