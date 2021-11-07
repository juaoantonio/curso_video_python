print("Digite 6 números inteiros e te mostrarei a soma apenas daqueles que forem pares!")

soma = 0

for x in range(1, 7):
    n = int(input('Digite o número inteiro: '))
    if n % 2 == 0:
        soma += n
print(soma)




