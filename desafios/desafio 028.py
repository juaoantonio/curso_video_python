import random as rd
from playsound import playsound

print('Irei pensar em um número de 1 a 10, tente adivinhar!')
numaleatorio = rd.randint(1, 10)
num = int(input('Em qual número pensei? '))

if num == numaleatorio:
    print(f'Boa! Acertou! O número em que pensei foi: {numaleatorio}')
else:
    print(f'Errou, que pena! O número que pensei foi: {numaleatorio}')
    playsound('/home/jaab/PycharmProjects/curso_em_video/desafios/errooou.wav')
