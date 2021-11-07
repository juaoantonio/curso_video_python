# Essa foi a forma que o professor Guanabara fez, usando o laço for
# (com alguns toques meus)

frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
numero_de_letras = len(frase)

inverso = ''

for letra in range(numero_de_letras - 1, -1, -1):
    inverso += frase[letra]

print(f'{frase} de modo inverso fica: {inverso}')
if frase == inverso:
    print('Temos um palíndromo!')

else:
    print('Não temos um palíndromo!')