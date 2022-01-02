print('='*100)
print('Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo entre 1 e 500.')
print('='*100)

#Resolução

#IMPORTANDO BIBLIOTECA
import math

#SOMANDO NÚMEROS ÍMPARES
print('===== Somando números ímpares =====')
soma = 0
for num in range(0, 501, 3):
    if num % 2 == 1:
        soma = soma + num #ou soma += 1
print(f'A soma dos números compreendidos na lista é igual a {soma}')

#print(' === FIM ===')