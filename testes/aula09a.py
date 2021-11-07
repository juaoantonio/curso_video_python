frase = 'Curso em Vídeo Python'

print(frase[1::2])

print(frase.upper().count('O'))

print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

# Percebe-se que a string é imutável

print(frase)

dividido = frase.split()
print('-'.join(dividido))
junto = '-'.join(frase)
print('' in frase)

print(dividido[2][3])
# O comando .split divide as strings em uma lista
# Nesse comando logo acima, estou pedindo para o Python me mostrar, no segundo elemento [2], o caractere [3]



