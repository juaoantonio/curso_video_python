from math import trunc

print('\033[1;97m')
print('=' * 50)
print('CONVERSOR DE BASES NUMÉRICAS'.center(50, '-'))
print('=' * 50)
print('\033[m')

# Definindo o número

numero = float(input('\033[32mDigite um número inteiro igual ou maior a zero: \033[m'))

# Testando se o número informado é inteiro e positivo

if numero != numero // 1 and numero < 0:
    print('Esse número não é inteiro! Refaça.')

else:

    # Definindo qual tipo de conversão de base é pedido

    numero_int = int(trunc(numero))

    print('\nEscolha uma das opções de conversão:')

    print('\t[1]\033[31m BINÁRIO\033[m')
    print('\t[2]\033[31m OCTAL\033[m')
    print('\t[3]\033[31m HEXADECIMAL\033[m')

    # Aplicando a conversão

    escolha = int(input('Qual sua escolha? '))

    if escolha == 1:
        print(f"{numero_int} em binário é igual a \033[34m{bin(numero_int)[2:]}")

    elif escolha == 2:
        print(f"{numero_int} em octal é igual a \033[034m{oct(numero_int)[2]}")

    elif escolha == 3:
        print(f"{numero_int} em hexadecimal é igual a \033[34m{hex(numero_int)[2]}")

    else:
        print('Essa não é uma opção válida!!! Tente novamente.')
