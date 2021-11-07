dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${total:.2f}')
