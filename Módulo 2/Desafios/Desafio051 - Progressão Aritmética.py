print('='*100)
print('Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.')
print('='*100)

#RESOLUÇÃO

num = int(input('Insira o primeiro termo da progressão aritmética: '))
raz = int(input('Qual é a razão da PA? '))
n = int(num + (11 - 1) * raz)
for num in range(num, n, raz):
    print(num)