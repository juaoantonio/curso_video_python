from random import randint
from time import sleep
from operator import itemgetter

print(' Valores sorteados para cada jogador '.center(50, '='))
sleep(1)
jogadores = {}

for c in range(1, 5):
    numero = randint(1, 6)
    jogadores[f'jogador {c}'] = numero
    print(f'O jogador {c} tirou {numero}')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()

print(' RANKING '.center(30, '='))
for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0].title()} com {v[1]}')
