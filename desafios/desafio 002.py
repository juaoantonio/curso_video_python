limpar = '\033[m'

estilo = {'none': '\033[0m',
          'negrito': '\033[1m',
          'sublinhado': '\033[4m',
          'invertido': '\033[7m'}


texto = {'preto': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'branco': '\033[97m'}

fundo = {'preto': '\033[40m',
         'vermelho': '\033[41m',
         'verde': '\033[42m',
         'amarelo': '\033[43m',
         'azul': '\033[44m',
         'roxo': '\033[45m',
         'ciano': '\033[46m',
         'cinza': '\033[47m',
         'branco': '\033[107m'}

dia=input('Dia: ')
mes=input('Mês: ')
ano=input('Ano: ')

print(f"{texto['azul']}Você nasceu no dia {texto['verde']}{dia}{texto['azul']}, do mês {texto['verde']}"
      f"{mes}{texto['azul']}, do ano {texto['verde']}{ano}")
