def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Quantos gols esse jogador fez? '))

if g.isnumeric():
    int(g)
else:
    g = 0

if n:
    ficha(n, g)

else:
    ficha(gols=g)
