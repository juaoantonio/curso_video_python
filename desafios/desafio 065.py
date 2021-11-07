from statistics import mean

parametro = ''
numeros = []

while parametro != 'n':
    num = int(input('\nDigite um número: '))
    numeros.append(num)

    parametro = str(input('Quer continuar? [S/N] ')).strip().lower()
    while parametro != 's' and parametro != 'n':
        print('Valor inválido!')
        parametro = str(input('Quer continuar? [S/N] \n')).strip().lower()

if len(numeros) == 1:
    print(f'Você só digitou 1 número: {numeros[0]}')
else:
    print(f'''
Você digitou um total de {len(numeros)} numeros.
A média desses números é igual a {mean(numeros)}.
O menor número digitado foi {min(numeros)} e o maior foi {max(numeros)}''')

