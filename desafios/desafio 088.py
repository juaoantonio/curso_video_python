from random import sample
from time import sleep

print('-' * 50)
print('< PALPITES DA MEGA SENA >'.center(50, '='))
print('-' * 50)

jogos = []
quantidade = int(input('Digite quantos jogos você quer que eu sorteie: '))
if quantidade > 0:
    for cont in range(0, quantidade):
        jogo = sample(range(1, 61), 6)
        jogo.sort()
        jogos.append(jogo[:])
        jogo.clear()

for cont in range(0, quantidade):
    print(f'Jogo {cont + 1}: {jogos[cont]}')
    sleep(1)
