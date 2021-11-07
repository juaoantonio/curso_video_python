from math import pow as p, sqrt as rq, hypot
c1 = float(input('Insira o valor do primeiro cateto: '))
c2 = float(input('Insira o valor do segundo: '))
h = hypot(c1, c2)
print(f'O valor da hipotenusa do triângulo retângulo é {h:.2f}')
