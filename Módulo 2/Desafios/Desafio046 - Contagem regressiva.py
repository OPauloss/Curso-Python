print('='*100)
print('Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.')
print('='*100)

#Resolução

#IMPORTANDO BIBLIOTECA
from time import sleep
from emoji import emojize

#CONTAGEM REGRESSIVA
print('=========== Contagem regressiva para o fim do ano! =============')
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print(emojize(':tada: Feliz ano novo! :tada:',use_aliases=True))