massa = float(input('Quanto mede sua massa em kg? '))
altura = float(input('Quanto mede sua altura em m? '))

imc = massa / (altura ** 2)
print(f'Seu Índice de Massa Corporal é igual a: {imc:.2f}')

if 0 < imc < 18.5:
    mensagem = 'Você está abaixo do peso!'

elif imc < 25:
    mensagem = 'Seu peso está ideal!'

elif imc < 30:
    mensagem = 'Você está com sobrepeso. Tome mais cuidado!'

elif imc < 40:
    mensagem = 'Você está com obesidade mórbida. Vá se tratar!!!'

elif imc >= 40:
    mensagem = 'Você está com um grande risco a sua saúde: obesidade mórbida!'

else:
    mensagem = 'Insira um valor válido!'

print(mensagem)
