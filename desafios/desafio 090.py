pessoa = {}

pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input('Média: '))

if 0 <= pessoa['media'] < 5:
    pessoa['situaçao'] = 'reprovado'

elif 5 <= pessoa['media'] <= 10:
    pessoa['situaçao'] = 'aprovado'

for k, v in pessoa.items():
    print(f'{k.title()} é igual a {v}')