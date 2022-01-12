# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

#Resolução
from random import randint
números = list()
def sorteia(lst):
    for num in range(0,5):
        lst.append(randint(0,100))
    print(f'Os números sorteados foram {números}')
def somaPar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares é {soma}')

sorteia(números)
somaPar(números)

    