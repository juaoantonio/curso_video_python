# Essa foi minha primeira forma de fazer :P

frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
numero_de_letras = len(frase)

invertido = frase[::-1]  # inverte a string
print(f'{frase} de forma invertida fica: {invertido}')

# Checando se a frase é um palíndromo
if frase == invertido:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

