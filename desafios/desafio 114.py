import requests

url = 'http://pudim.com.br'

try:
    requests.head(url)

except requests.exceptions.ConnectionError:
    print(f'\033[31mNão consegui acessar o site {url}! :(\033[m')

else:
    print(f'Consegui me conectar ao site {url} com sucesso!')
