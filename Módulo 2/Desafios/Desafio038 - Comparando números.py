print('='*100)
print('''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
→ O primeiro valor é maior
→ O segundo valor é maior
→ Não existe valor maior, os dois são iguais''')
print('='*100)

#Resolução

# Lendo dois números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#Descobrindo qual número é maior
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}')
else:
    print('Os dois números são iguais')