print('='*100)
print('''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
→ Equilátero: todos os lados iguais
→ Isósceles: dois lados iguais
→ Escaleno: todos os lados diferentes. ''')
print('='*100)

#Resolução
#Capturando a entrada do usuário
a = float(input('Digite o comprimento do lado A: '))
b = float(input('Digite o comprimento do lado B: '))
c = float(input('Digite o comprimento do lado C: '))

#Calculando
from math import fabs
triangulo = fabs(b - c) < a < b + c

if triangulo == True and (a == b == c):
    print(f'Com os valores {a}, {b} e {c}, é possível formar um triângulo EQUILÁTERO.')
elif triangulo == True and (a != b != c):
    print(f'Com os valores {a}, {b} e {c} é possível formar um triângulo ESCALENO')
elif triangulo == True:
    print(f'Com os valores {a}, {b} e {c}, é possível formar um triângulo ISÓSCELES')
else:
    print('Não é possível formar um triângulo com os valores inseridos.')
