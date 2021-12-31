print('='*100)
print('Crie um programa que faça o computador jogar Jokenpô com você.')
print('='*100)

#Resolução

#importando biblioteca emoji
from emoji import emojize
import random
import time

#Capturando a entrada do usuário e PC
player = int(input(emojize('Vamos jogar Jokenpô!\nDigite 1 para :punch:\nDigite 2 para :raised_hand:\nDigite 3 para :scissors:\n\n---> ', use_aliases=True)))
pc = random.randint(1,3)


#Traduzindo valores
if player == 1 and pc == 1:
    print(emojize('Você escolheu PEDRA. :punch:', use_aliases=True))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('PEDRA. :punch:\n -- EMPATE --',use_aliases=True))
elif player == 1 and pc == 2:
    print(emojize('Você escolheu PEDRA. :punch:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('PAPEL! :raised_hand:\n -- VOCÊ PERDEU --'))
elif player == 1 and pc == 3:
    print(emojize('Você escolheu PEDRA. :punch:',use_aliases=True))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('TESOURA! :scissors:\n -- VOCÊ VENCEU --'))
elif player == 2 and pc == 1:
    print(emojize('Você escolheu PAPEL. :raised_hand:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('PEDRA! :punch:\n -- VOCÊ VENCEU --',use_aliases=True))
elif player == 2 and pc == 2:
    print(emojize('Você escolheu PAPEL. :raised_hand:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('PAPEL! :raised_hand:\n -- EMPATE --'))
elif player == 2 and pc == 3:
    print(emojize('Você escolheu PAPEL. :raised_hand:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('TESOURA! :scissors:\n -- VOCÊ PERDEU --'))
elif player == 3 and pc == 1:
    print(emojize('Você escolheu TESOURA. :scissors:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('PEDRA! :punch:\n -- VOCÊ PERDEU --',use_aliases=True))
elif player == 3 and pc == 2:
    print(emojize('Você escolheu TESOURA. :scissors:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('PAPEL! :raised_hand:\n -- VOCÊ GANHOU --'))
else:
    print(emojize('Você escolheu TESOURA. :scissors:'))
    time.sleep(0.5)
    print('O computador jogou...')
    time.sleep(2)
    print(emojize('TESOURA! :scissors:\n -- EMPATE --'))