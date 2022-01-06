print('='*50)
print('''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.''')
print('='*50)

from random import randint

#pc1 = randint(0, 10)
#pc2 = randint(0, 10)
#pc3 = randint(0, 10)
#pc4 = randint(0, 10)
#pc5 = randint(0, 10)
#num = pc1, pc2, pc3, pc4, pc5
#lista = sorted(num)
#print(f'Foram gerados 5 números aleatórios: {num}')
#print(f'O menor valor da lista é {(lista[0])} e o maior é {lista[4]}')

#Outra maneira de fazer
num = (randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10))
print(f'Foram gerados 5 números aleatórios: {num}')
print(f'O maior valor da lista é {max(num)}')
print(f'O menor valor da lista é: {min(num)}')
