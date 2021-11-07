r = ''
while r != 'm' and r != 'f':
    r = str(input('Qual seu sexo? [M/F] ')).strip().lower()
    if r != 'm' and r != 'f':
        print('Insira um valor válido!\n')

if r == 'm':
    print('Seu sexo é masculino.')

elif r == 'f':
    print('Seu sexo é feminino.')
