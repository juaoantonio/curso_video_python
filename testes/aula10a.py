nome = str(input('Qual é seu nome? ')).strip().lower()
if nome == 'joão':
    print('Que nome lindo você tem!!!')
else:
    print('(Seu nome é tão normal...)')
print(f'Olá, {nome.title()}!')
