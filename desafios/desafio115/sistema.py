from lib.arquivo import *
from time import sleep

arq = 'dados_usuarios.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    opcoes = [
        '\033[1;92mVer pessoas cadastradas\033[m',
        '\033[1;92mCadastrar novas pessoas\033[m',
        '\033[1;92mSair do programa\033[m',
    ]
    menu(opcoes)

    opcao_usuario = opcoes_menu('\033[1;34mDigite a opção de sua escolha: \033[m', 1, 2, 3)

    if opcao_usuario == 1:
        ler_arquivo(arq)
        sleep(2)

    elif opcao_usuario == 2:
        cadastro_usuario(arq)
        sleep(2)
    elif opcao_usuario == 3:
        titulo('OBRIGADO, VOLTE SEMPRE!', 13)
        sleep(1)
        break
