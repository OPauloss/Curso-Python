print('='*80)
print('''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu''')
print('='*80)

#Resolução

#Capturando a entrada do usuário
num = int(input('Tente adivinhar o número gerado pelo computador! Digite um valor entre 0 e 5: '))

#Gerando um número entre 0 e 5:
from random import randrange
pc = randrange(start=0, stop=5)

#Determinando condições
if num > 5:{
    print('Erro: o número digitado deve estar entre 0 e 5!')
}
if num == pc:{
    print(f'O número digitado foi {num} e o valor gerado pelo computador foi {pc}.Parabéns! Você acertou o número! :)')
}
else:{
    print(f'O número digitado foi {num} e o valor gerado pelo computador foi {pc}. Que pena, você errou. :/')
}
