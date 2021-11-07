ano = int(input('Diga qual ano você está e eu direi se ele é bissexto ou não: '))
bissexto = ano % 4
if bissexto == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')
