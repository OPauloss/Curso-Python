print('='*80)
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.')
print('='*80)

#Resolução
from math import hypot

cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é {hypot(cato, cata)}')


# O quadrado da hipotenusa é igual a soma dos quadrados dos catetos