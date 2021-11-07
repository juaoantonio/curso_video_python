valores = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    continuar = ''

    while continuar != 's' and continuar != 'n':
        continuar = input('Gostaria de continuar? [S/N] ')

        str(continuar).strip().lower()
        if continuar != 's' and continuar != 'n':
            print('Não entendi, tente novamente!')

    if continuar == 's':
        print()
        pass
    elif continuar == 'n':
        print()
        break

valores.sort(reverse=True)

print(f'Você digitou {len(valores)} valores')
print(f'Aqui está a ordem decrescente dos valores digitados: {valores}')

if 5 not in valores:
    print('Não encontrei o valor 5!')
else:
    print('O valor 5 aparece na lista!')
