import random
n1 = input('Nome do primeiro: ')
n2 = input('Nome do segundo: ')
n3 = input('Nome do terceiro: ')
n4 = input('Nome do quarto: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação será: \n{lista}')