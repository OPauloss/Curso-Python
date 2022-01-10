# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Resolução



jogador = dict()
gols = []

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
jogador['partidas'] = int(input(f'{jogador["nome"]} jogou quantas partidas? --> '))
for partida in range(0,(jogador['partidas'])):
    gols.append(int(input(f'Quantos gols na partida {partida}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for partida in range(jogador['partidas']):
    print(f'--> Na partida {partida} fez {gols[partida]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
