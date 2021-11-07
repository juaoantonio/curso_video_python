# Sequência de Fibonacci
print('\\' * 25, '/' * 25)
print('    SEQUÊNCIA DE FIBONACCI    '.center(50, '|'))
print('\\' * 25, '/' * 25)

print()
quantidade_de_termos = int(input('Digite a quantidade de termos da sequência desejados: '))

f1 = 0
f2 = 1

contador = 1

while contador <= quantidade_de_termos:
    print(f'{f1} =>', end=' ')
    soma = f1 + f2
    f1 = f2
    f2 = soma
    contador += 1

print('Fim')
