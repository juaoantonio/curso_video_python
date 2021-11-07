print('=' * 50)
print('10 PRIMEIROS TERMOS DE UMA PA'.center(50))
print('=' * 50)

primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão: '))

print('Esses são os primeiros 10 dez termos dessa progressão:')
termo = primeiro_termo
cont = 0
quantidade_de_termos = 10

while cont != quantidade_de_termos:  # A princípio, a quantidade de termos é 10
    print(f'{termo} =>', end=' ')
    termo += razao
    cont += 1  # A contagem dos termos e as repetições são definidas aqui

    if cont == quantidade_de_termos:
        print('PAUSA')
        quantidade_de_termos += int(input('Quantos termos você quer mostrar a mais? '))
        # A quantidade de termos é aumentada, caso o usuário digite um valor maior que 0, prolongando a repetição

print(f'A progressão foi finalizada com {cont} termos mostrados. ')

