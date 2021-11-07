expressao = str(input('Digite uma expressão: '))
pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')

    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print(f'A expressão {expressao} é válida!')
else:
    print(f'A expressão {expressao} é inválida!')
