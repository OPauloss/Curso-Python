print('='*100)
print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.')
print('='*100)

#Lendo a entrada do usuário

num = int(input('Número: '))
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        print(f'O número {num} é primo')
elif num == 2 or num == 3 or num == 5 or num == 7:
        print(f'O número {num} é primo')
else:
        print(f'O número {num} NÃO é primo')

# Não é necessário usar laços de repetição nesse exercício...
