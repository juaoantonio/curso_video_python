km = float(input('Quantos km terá sua viagem? '))
total = int(km)
if total <= 200:
    final = total * 0.5
else:
    final = total * 0.45
print(f'Você pagará, no total, R${final:.2f}')