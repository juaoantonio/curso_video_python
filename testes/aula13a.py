from time import sleep

# Repetição simples:
for c in range(1, 6):
    print('Olá!')
print('FIM')

print()
# Contagem regressiva:
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print()

# Pedindo para o usuário definir os valores do range do laço for:
inicio = int(input('Defina o valor inicial (inteiro): '))
final = int(input('Defina um valor final (inteiro): '))
intervalo = int(input('Escolha um intervalo para a contagem (inteiro): '))

for c in range(inicio, final+1, intervalo):
    print(c)
