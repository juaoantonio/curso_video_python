from random import randint
print('-' * 50)
print('Vamos jogar Par ou Ímpar!!!')
print('-' * 50)
cont = 0

while True:
    valor = int(input('Digite um valor: '))

    par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).strip().lower()

    if par_ou_impar != 'p' and par_ou_impar != 'i':
        print('Digite um valor válido!')

    else:
        computador = randint(0, 10)

        print('-' * 50)
        soma = valor + computador
        if soma % 2 == 0:
            print(f'Você escolheu {valor} e o computador escolheu {computador}')
            print(f'O total foi {soma}: \033[34mPAR\033[m')
            if par_ou_impar == 'p':
                print('Sua escolha foi par. \033[32mVocê venceu!\033[m')
                print('-' * 50)
                cont += 1

            else:
                print('Sua escolha foi ímpar. \033[31mVocê perdeu!\033[m')
                print('-' * 50)
                break

        else:
            print(f'Você escolheu {valor} e o computador escolheu {computador}')
            print(f'O total foi {soma}: \033[31mÍMPAR\033[m')
            if par_ou_impar == 'i':
                print('Sua escolha foi ímpar. \033[32mVocê venceu!\033[m')
                print('-' * 50)
                cont += 1

            else:
                print('Sua escolha foi par. \033[31mVocê perdeu!\033[m')
                print('-' * 50)
                break

if cont <= 5:
    print(f'GAME OVER! Você ganhou {cont} vezes.')

elif cont > 5:
    print(f'UAU! Você venceu mais de 5 vezes, parabéns!')
