def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando todos os valores {valores}, temos {s}')


soma(5, 6, 1, 3, 12)
