from random import sample
numeros = tuple(sample(range(1, 11), 5))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nMenor número é {min(numeros)}')
print(f'Maior número é {max(numeros)}')