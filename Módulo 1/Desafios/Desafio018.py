print('='*80)
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
print('='*80)

#Resolução
import math

angulo = float(input('Digite o ângulo para saber quais são os seus seno, cosseno e tangente: '))
print(f'Os valores de um ângulo de {angulo}ºC são os seguintes:\nSeno: {math.sin(math.radians(angulo))}\nCosseno: {math.cos(math.radians(angulo))}\nTangente: {math.tan(math.radians(angulo))}')

# Não tinha certeza de quais eram os módulos, então importei a biblioteca math inteira.