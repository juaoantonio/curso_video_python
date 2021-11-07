from time import sleep

c = ('\033[m',          # 0 - sem cor
     '\033[1;97;41m',   # 1 - texto preto com fundo vermelho
     '\033[1;97;42m',   # 2 - texto branco com fundo verde
     '\033[1;30;107m',  # 3 - texto preto com fundo branco
     '\033[1;97;46m')   # 4 - texto branco com fundo azul


def ajuda(a):
    titulo(f'Acessando o manual do comando ({comando})', cor=4)
    sleep(1)
    print(c[3], end='')
    help(a)
    print(c[0], end='')
    sleep(1)


def titulo(msg: str, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(msg.center(len(msg) + 4))
    print('~' * (len(msg) + 4))
    print(c[0], end='')


# Programa Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2)
    comando = str(input('Função ou Biblioteca >>> ')).lower().strip()
    if comando.lower().strip() == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', cor=1)
