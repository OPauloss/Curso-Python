# Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada
# a) De 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

from time import sleep

def contador():
    print('Contagem de 1 até 10 de 1 em 1')
    for num in range(1,11):
        print(num)
        sleep(0.25)
    print('FIM')
    print('-='*50)
    print('Contagem de 10 até 0 de 2 em 2')
    for num in range(10,-1,-2):
        print(num)
        sleep(0.25)
    print('FIM')
    print('-='*50)
    print('Agora é sua vez de personalizar a contagem:')
    a = int(input('Início: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    if not c:
        c = 1
    if a > b and c > 0:
        c = -c
    print('-='*50)
    for num in range(a, b-1 if c < 0 else b+1, c):
        print(num)
        sleep(0.25)
    print('FIM')


contador()
