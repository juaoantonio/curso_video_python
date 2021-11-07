palavras = ('MUNDO',
            'PROGRAMADOR',
            'PROGRAMAÇÃO',
            'CURSO')

for palavra in palavras:
    print(f'A palavra {palavra} tem as vogais', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
    print()
