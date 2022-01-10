#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter # Esta biblioteca permite ordenar os elementos de um dicionário/lista.
jogadores = {'Jogador 1':'','Jogador 2':'','Jogador 3':'','Jogador 4':''}
n = 0


print(f"{'Valores sorteados':^15}")
for i in range(1,5):
    dado = randint(1,6)
    jogadores[f'Jogador {i}'] = dado
    print(f'Jogador {i} tirou {dado} no dado')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*50)
print(f"{'== RANKING DOS JOGADORES ==':^5}")
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)

#Linha16: Os elementos do dicionário foram colocados em uma lista e postos em ordem, através do módulo operator "itemgetter"

