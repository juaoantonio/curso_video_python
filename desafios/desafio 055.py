pesos = []

for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    pesos.append(peso)

pesos.sort()
print(f"""O menor peso é {pesos[0]}
O maior peso é {pesos[-1]}""")
