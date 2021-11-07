# Faça um conversor de Celsius para Fahrenheit para Celsius
c = float(input('Informe um valor em ºC para ser convertido em Fº e Kº: '))

f = (c * 1.8) + 32
k = c + 273.15

print(f'{c}ºC é equivalente a {f:.1f}ºF e {k:.1f}ºK')
