# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site não está disponível no momento. Tente mais tarde.')
else:
    print('\033[33mConexão com o site estabelecida com sucesso.\033[m')
