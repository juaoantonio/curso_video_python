def cabecalho(msg):
    print('=-=' * 15)
    print(str(msg).center(45))
    print('=-=' * 15)


jogadores = list()
jogador = dict()
gols = list()

cabecalho('CADASTRO DE JOGADORES')
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()

    num_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, num_partidas):
        gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if continuar in 'sn':
            break
        print('Valor inválido! Por favor, digite somente S ou N')
    if continuar == 'n':
        print()
        break

cabecalho('TABELA DE INFORMAÇÕES')

print(f"{'Cod':<5} {'Nome':<10} {'Gols':<15} {'Total':<10}")
for c in range(len(jogadores)):
    print(f"  {c:<3} {str(jogadores[c]['nome']):<10} {str(jogadores[c]['gols']):<15} {str(jogadores[c]['total']):<10}")

while True:
    opcao = int(input('\nMostrar dados de qual jogador? [999 para interromper]: '))
    if 0 <= opcao <= len(jogadores) - 1:
        print(f'Levantamento do jogador {jogadores[opcao]["nome"]}')
        for i, v in enumerate(jogadores[opcao]['gols']):
            print(f'    No jogo {i + 1}, fez {v} gols')

    elif opcao == 999:
        break

    else:
        print('Jogador não existente!')
print('\nPrograma encerrado!')
