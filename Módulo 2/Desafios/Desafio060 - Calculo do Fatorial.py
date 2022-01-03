print('''Faça um programa que leia um número qualquer e mostre o seu fatorial. Utilizando o "while" e o "for"
Ex. 5! = 5x4x3x2x1 = 120''')
print('='*100)

#Resolução
print(' =============== CALCULO FATORIAL ===============')
num = int(input('Digite um número: '))
res = 1

#for i in range(num, 1, -1):
#    print(f'{i}x', end='')
#    res *= i
#print(f'1: {res}')
#print('=========================================================')


while num > 1:
    print(f'{num}x', end='')
    res *= num
    num -= 1   
print(f'1: {res}')
#print ("=========================================================")

    