num = int(input('Digite um número e direi se ele é ímpar ou par: '))
imparoupar = num % 2
if imparoupar == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')
