salario = float(input('Qual o salário do funcionário? '))

if salario <= 1250.00:
    final = salario + salario * (15 / 100)
    print(f'O salário terá um acréscimo de 15%, e será igual a R${final:.2f}')
else:
    final = salario + salario * (10 / 1000)
    print(f'O salário terá um acréscimo de 10%, e será igual a R${final:.2f}')
