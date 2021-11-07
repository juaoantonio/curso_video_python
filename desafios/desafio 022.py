nome = str(input('Qual seu nome completo? ')).strip()

print(f'Seu nome em caixa alta é assim: {nome.upper()}')
print(f'Seu nome em caixa baixa é assim: {nome.lower()}')
letras = len(nome) - nome.count(' ')
print(f'Seu nome tem {letras} letras')

dividido = nome.split()
primeironome = len(dividido[0])

print(f'Seu primeiro nome tem {primeironome} letras')
