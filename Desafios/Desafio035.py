print('='*80)
print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')
print('='*80)

#Resolução

#Capturando a entrada do usuário
a = float(input('Digite o comprimento do lado A: '))
b = float(input('Digite o comprimento do lado B: '))
c = float(input('Digite o comprimento do lado C: '))

#Calculando
import math

if math.fabs(b - c) < a < b + c:{
    print(f'Com os valores {a}, {b} e {c}, é possível formar um triângulo.')
}
else:{
    print('Não é possível formar um triângulo com os valores inseridos.')
}