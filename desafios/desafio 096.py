def area(com, larg):
    print(f'A área de {com}m x {larg}m é igual a {com * larg}m²')


print('Controle de Terrenos'.center(50))
print('-' * 50)
comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))

area(comprimento, largura)
