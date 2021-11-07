print('=' * 50)
print('10 PRIMEIROS TERMOS DE UMA PA'.center(50))
print('=' * 50)

primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão: '))

print('Esses são os primeiros 10 dez termos dessa progressão:')
termo = primeiro_termo
cont = 0

while not cont == 10:
    print(f'{termo} =>', end=' ')
    termo += razao
    cont += 1

print('FIM DA PROGRESSÃO')
