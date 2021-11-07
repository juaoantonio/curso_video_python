print('=' * 50)
print('10 PRIMEIROS TERMOS DE UMA PA'.center(50))
print('=' * 50)

primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão: '))
quantidade_de_termos = int(input('Digite quantos termos você quer que apareçam: '))

print()

print(f'Esses são os primeiros {quantidade_de_termos} termos dessa progressão:')
for n in range(0, quantidade_de_termos):
    termo = primeiro_termo + razao * n
    print(f'{termo}', end=' => ')
print('FIM DA PROGRESSÃO')
