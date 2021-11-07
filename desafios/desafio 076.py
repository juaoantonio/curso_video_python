listagem = ('Lápis', 1.75,
            'Caneta', 2.00,
            'Lapizeira', 5.00)

for i in range(0, len(listagem) - 1, 2):
    print(f'{listagem[i]} '.ljust(25, '.'), f'R$ {listagem[i + 1]:.2f}')
