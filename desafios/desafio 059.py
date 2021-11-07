from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
lista = [num1, num2]

opcao = 0

while opcao != 5:

    print('''\nEscolha uma opção:
    [1] Somar 
    [2] Multiplicar
    [3] Maior número
    [4] Novos números
    [5] Sair do programa''')

    opcao = int(input('Qual sua escolha? '))
    print()
    if opcao == 1:
        print(f'A soma entre {num1} e {num2} é igual a {num2 + num1}')
        sleep(1.5)

    elif opcao == 2:
        print(f'A mulpicação de {num1} vezes {num2} é igual a {num1 * num2}')
        sleep(1.5)

    elif opcao == 3:
        if num1 == num2:
            print('Os números são iguais!')
        else:
            print(f'O maior número é {max(lista)}')
        sleep(1.5)

    elif opcao == 4:
        print('Insira novamente os números:')
        num1 = int(input('Digite o primeiro valor novamente: '))
        num2 = int(input('Digite o segundo valor novamente: '))

    elif opcao == 5:
        print('Encerrando o programa...')
        sleep(3)

    else:
        print('Valor inválido! Tente novamente.')

print('Programa encerrado, volte sempre!')
