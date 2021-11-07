a = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura dela em metros? '))

area = l * a
print(f'Sabendo que cada litro de tinta pinta uma área de 2m², você precisará de {round(area / 2):.1f} litros de tinta, '
      'aproximadamente. =)')
