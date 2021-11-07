import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de {moeda.formatacao(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.formatacao(p)} é {moeda.formatacao(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.diminuir(p, 10))}')
print(f'Diminuindo 15%, temos {moeda.formatacao(moeda.diminuir(p, 15))}')
