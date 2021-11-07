# Joquenpô Game
import time
import random as rd
from emoji import emojize

opcoes = [1, 2, 3]  # 1 = pedra, 2 = papel, 3 = tesoura
pedra = emojize(':raised_fist:')
papel = emojize(':raised_hand:')
tesoura = emojize(':victory_hand:')

texto = f"""
\033[32mVamos brincar de Joquenpô\033[m!!!

Escolha um desses:
\033[31m[1] Pedra\033[m {pedra}
\033[31m[2] Papel\033[m {papel}
\033[31m[3] Tesoura\033[m {tesoura}"""
print(texto)

escolha_do_usuario = int(input('===> '))

# Aqui, a máquina escolhe sua opção:
escolha_da_maquina = rd.choice(opcoes)

if escolha_da_maquina == 1:
    print('Escolhi pedra.')

elif escolha_da_maquina == 2:
    print('Escolhi papel.')

elif escolha_da_maquina == 3:
    print('Escolhi tesoura.')

time.sleep(1)
print()

# Resultados
if escolha_do_usuario == escolha_da_maquina:
    print('Deu empate, vamos de novo!')

elif escolha_do_usuario == 1 and escolha_da_maquina == 2:
    print('Papel ganha de pedra! Ganhei!')

elif escolha_do_usuario == 3 and escolha_da_maquina == 1:
    print('Pedra ganha de tesoura! Ganhei!')

elif escolha_do_usuario == 2 and escolha_da_maquina == 3:
    print('Tesoura ganha de papel! Ganhei!')

elif escolha_do_usuario == 1 and escolha_da_maquina == 3:
    print('Droga, pedra ganha de tesoura! Perdi!')

elif escolha_do_usuario == 2 and escolha_da_maquina == 1:
    print('Droga, papel ganha de pedra! Perdi!')

elif escolha_do_usuario == 3 and escolha_da_maquina == 2:
    print('Droga, tesoura ganha de papel! Perdi!')
