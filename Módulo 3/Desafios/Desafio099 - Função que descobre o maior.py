# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

#Resolução
from time import sleep

def maior(*num):
    print('Analisando os valores passados: ')
    sleep(1)
    for valor in num:
        print(valor, end=' ',flush=True)
        sleep(0.25)
    print(f'. Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('=-'*20) 


maior(55,6,45,75,1,0,3,6,9,4,10)
maior(4,7,0)
maior(6)