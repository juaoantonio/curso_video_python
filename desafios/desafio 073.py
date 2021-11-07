times = ('atlético-mg', 'palmeiras', 'fortaleza', 'flamengo', 'bragantino',
         'corinthians', 'internacional', 'fluminense', 'athletico-pr', 'cuiabá',
         'ceará', 'atlético-go', 'são paulo', 'juventude', 'américa-mg', 'santos',
         'bahia', 'grêmio', 'sport', 'chapecoense')

print(' LISTAS DAS 20 PRIMEIRAS POSIÇÕES DOS TIMES DO BRASILEIRÃO '.center(100, '~'))

while True:
    menu = '''
    Escolha uma opção: 
    [1] Apresentar a ordem de classificação
    [2] Os cinco primeiros classificados
    [3] Os quatro últimos classificados
    [4] Em ordem alfabética
    [5] O time de determinada posição
    [0] Sair do programa 
    '''
    print(menu)

    opcao = str(input('Escolha uma opção: ')).strip()

    print('=' * 50)
    if opcao not in '012345':

        print('Valor invaĺido!')
        print('=' * 50)

    opcao = int(opcao)
    if opcao == 1:
        print('Ordem de classificação:\n')
        for pos, time in enumerate(times):
            print(f'{pos + 1}º: {time.upper()}')

    if opcao == 2:
        print('Os cinco primeiros:\n')
        for pos, time in enumerate(times[:5]):
            print(f'{pos + 1}º: {time.upper()}')

    if opcao == 3:
        print('Os quatros últimos:\n')
        for pos, time in enumerate(times[-4:len(times)]):
            print(f'{pos + 17}º: {time.upper()}')

    if opcao == 4:
        print('Em ordem alfabética:\n')
        for time in sorted(times):
            print(time.upper())

    if opcao == 5:
        while True:
            pos = int(input('De qual classificação você quer saber o time? ')) - 1
            if 0 <= pos <= 19:
                print(f'\033[31m{str(times[pos]).title()} está na {pos + 1}ª posição.\033[m')
                break
            else:
                print('Insira um valor de 1 a 20!')

    if opcao == 0:
        break

print('Fim do programa! Volte sempre!')