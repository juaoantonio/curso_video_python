galera = []
dado = []

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    print(f'{pessoa[0]} têm {pessoa[1]} anos de idade')