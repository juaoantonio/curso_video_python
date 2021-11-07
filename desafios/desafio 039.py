from datetime import date

# Determinando o sexo

print("""Você é homem ou mulher?
[1] Homem
[2] Mulher""")

sexo = input('==> ')

if sexo == '2':
    print('Você não precisa se alistar obrigatoriamente!')

elif sexo == '1':
    nascimento = int(input('Em qual ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    print(f'Você, que nasceu em {nascimento}, tem {idade} anos nesse ano de {ano_atual}')

    if idade < 18:
        restante = 18 - idade
        print(f'Você só poderá se alistar daqui a {restante} ano(s)')
        print(f'Seu alistamento será em {nascimento + 18}')

    elif idade > 18:
        ano_do_alistamento = nascimento + 18
        anos_a_mais = idade - 18

        print(f'Você já deveria ter se alistado há {anos_a_mais} anos')
        print(f'Seu alistamento deveria ter sido em {ano_do_alistamento}')

    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!!!')

else:
    print('Esse não é um valor válido!')