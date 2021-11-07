nome = str(input('Qual seu nome? '))

if nome == 'João':
    print('\033[32mQue nome legal!')
elif nome == 'Samira':
    print('\033[1;36mAcho que nunca ouvi nome mais bonito!')
# Pode-se usar o elif mais de uma vez
else:
    print('\033[31mMais um nome normal...')
# Já o else, somente uma ou nenhuma vez
print(f'\033[mTenha um bom dia, {nome}!')
