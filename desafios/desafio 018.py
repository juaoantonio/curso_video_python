from math import tan, sin, cos, radians as rad
ang = float(input('Digite o ângulo que você deseja: '))
s = sin(rad(ang))
c = cos(rad(ang))
tg = tan(rad(ang))
print(f'O SENO de {ang} é igual a {s:.2f}')
print(f'O COSSENO de {ang} é igual a {c:.2f}')
print(f'A TANGENTE de {ang} é igual a {tg:.2f}')