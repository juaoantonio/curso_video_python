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

nome = input(f"Olá! Tudo bem? {texto['vermelho']}Poderia me dizer qual seu nome? {limpar}")
print(f"E aí,{texto['azul']} {nome}{limpar}, seja bem-vindo!")
