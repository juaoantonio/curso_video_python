def leia_dinheiro(mensagem: str = ''):
    while True:
        valor = input(f'{mensagem}').strip()
        if ',' in valor:
            valor = valor.replace(',', '.')

        try:
            float(valor)
            return float(valor)

        except ValueError:
            print(f'\033[31mERRO! {valor} é um preço inválido\033[m')


def leia_int(a: str):
    while True:
        try:
            valor = int(input(a))

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')

        except KeyboardInterrupt:
            print('\nO usuário não quis mais executar o programa :(')
            exit()

        else:
            return int(valor)


def leia_float(a: str):
    while True:
        try:
            valor = float(input(a))

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido!\033[m')

        except KeyboardInterrupt:
            print('\nO usuário não quis mais executar o programa :(')
            exit()

        else:
            return int(valor)
