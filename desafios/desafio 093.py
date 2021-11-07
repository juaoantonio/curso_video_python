jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()

num_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, num_partidas):
    gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('=--=' * 10)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=--=' * 10)
print(f'O jogador {jogador["nome"]} jogou {num_partidas} partidas.')
for c in range(0, num_partidas):
    print(f'    => Na partida {c + 1}, {jogador["nome"]} fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols')