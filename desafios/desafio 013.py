# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com x% de aumento

salario_antigo = float(input('Qual o salário anterior do funcionário? R$'))
aumento = float(input('Em quantos porcento está sendo aumentado? '))

salario_novo = salario_antigo + salario_antigo * (aumento / 100)

print(f'O novo salário do funcionário é de R${salario_novo:.2f}')