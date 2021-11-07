# Faça um progrma que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

valor = input('Digite algo para te dar informações sobre: ')

print('A informação dada é um tipo primitivo:', type(valor))
print('Aqui, "True" significa "sim" e "False" significa "não" ;)')

print('É alfabético-numérico?', valor.isalnum())
print('É composto todo por letras minúsculas?', valor.islower())
print('É composto só por valores alfabéticos?', valor.isalpha())
print('É composto só por números?', valor.isnumeric())
