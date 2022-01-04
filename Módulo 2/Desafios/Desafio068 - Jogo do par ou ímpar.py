print('Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.')
print('='*50)

import random

print('='*50)
print('PAR OU IMPAR')
print('='*50)
cont = 1
while True:
    player = int(input('Digite um valor: '))
    option = str(input('Você quer PAR ou ÍMPAR? [P/I]')).strip().lower()[0]
    pc = random.randint(0, 10)
    soma = player + pc
    if soma % 2 == 0:
        print(f'Você jogou {player} e o computador jogou {pc}. Total de {soma}. DEU PAR')
        if option == 'p':
            print('Você GANHOU.\nVamos jogar de novo...')
            cont += 1
        elif option == 'i':
            print(f'Você PERDEU\nGame Over! Você jogou {cont} vezes')
            break
    else:
        print(f'Você jogou {player} e o computador jogou {pc}. Total de {soma}. DEU ÍMPAR')
        if option == 'i':
            print('Você GANHOU.\nVamos jogar de novo...')
            cont +=1
        elif option == 'p':
            print(f'Você PERDEU\nGame Over! Você jogou {cont} vezes')
            break

        