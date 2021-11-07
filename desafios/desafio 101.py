def voto(nascimento=0):
    from datetime import date
    idade = date.today().year - nascimento

    if idade < 16:
        status = 'NÃO VOTA'

    elif 18 <= idade < 65:
        status = 'VOTO OBRIGATÓRIO'

    else:
        status = 'VOTO OPCIONAL'

    return f'Com {idade} anos: {status}.'

# Programa Principal
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
print(voto(ano_nascimento))
