print('Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo. cadastrando tudo em uma lista composta.')

#Resolução

from random import randint
from time import sleep

aposta = []
jogos = []

qtd = int(input('Quantos jogos você quer gerar? ---> '))
print(f'{"POSSÍVEIS PALPITES PARA A MEGA-SENA"}')

while qtd > 0:
    for n in range(0,6):
        num = randint(1,60)
        while num in aposta:
            num = randint(1,60)
        aposta.append(num)
    jogos.append(sorted(aposta[:]))
    aposta.clear()
    qtd -= 1
    print(jogos)
    jogos.clear()
    sleep(1)