# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Resolução



jogador = dict()
gols = []
lista = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? : '))
    for p in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {p}?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    while resp not in 'SsNn':
        print('ERRO: Por favor, digite apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
print()
print('-='*30)
for k, v in enumerate(lista):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

