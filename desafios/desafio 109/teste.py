import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de {moeda.formatacao(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.formatacao(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(p, 15, True)}')
