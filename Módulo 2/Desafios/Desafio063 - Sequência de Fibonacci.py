print('''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
ex: 0 → 1 → 1 → 2 → 3 → 5 → 8 ''')
print('='*100)

#Resolução
print('============= Sequência de Fibonacci =============')
import math

cont = 3
t1 = 0
t2 = 1
num = float(input('Quantos termos você quer mostrar?  ' ))
print(f'{t1} → {t2}', end='')
while cont <= num:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\n===== FIM DO PROGRAMA =====')