print('Melhore o jogo do desafio028, onde o computador vai "pensar" em um número de 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.')
print('='*100)

#Resolução
from random import randint

cont = 0
soma = 0

while cont == 0:
    player = int(input('Digite um número de 0 a 10: '))
    pc = randint(0, 10)

    if player == pc:
        print(f'O Computador pensou em {pc}, você pensou em {player}. Parabéns, você GANHOU!!')
        print(f'Foram necessárias {soma} tentativas para vencer.')
        cont = 1
    elif player != pc:
        print (f'O Computador pensou em {pc}, você pensou em {player}. Que pena, você ERROU!')
        soma += 1