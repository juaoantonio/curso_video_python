n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda: '))
m = (n1 + n2) / 2
print(f'A média das notas é {m:.2f}')
if m <= 5.0:
    print('Alguém está precisando estudar mais...')
if 5.0 < m <= 7.5:
    print('Tá okay, mas pode melhorar.')
if m > 7.5:
    print('Ótimo! Você está no caminho certo!')
