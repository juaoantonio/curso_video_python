print('Me deixe saber se você ultrapassou o limite de velocidade.')
print('Lembrando que a cada km a mais do limite, você paga 7 reais.')
km = float(input('Diga-me qual foi a velocidade máxima que você obteve: '))
if km > 80:
    multa = (km - 80.0) * 7
    print(f'Você passou do limite de velocidade! Sua multa custará R${multa:.2f}')
else:
    print('Você estava dentro dos limites. Continue assim!')