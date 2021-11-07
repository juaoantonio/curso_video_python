import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de R${p} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p} é R${moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 15%, temos R${moeda.diminuir(p, 15)}')
