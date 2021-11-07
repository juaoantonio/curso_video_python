numeros_extenso = ('zero', 'um', 'dois', 'três','quatro','cinco',
                   'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                   'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero_usuario = int(input('Digite um número entre 0 e 20: '))

    if 0 <= numero_usuario <= 20:
        break

    else:
        print('Valor inválido! Tente novamente!')

print(f'Você digitou o número {numeros_extenso[numero_usuario]}')