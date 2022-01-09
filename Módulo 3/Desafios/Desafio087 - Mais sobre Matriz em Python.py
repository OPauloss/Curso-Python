#print('''Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.''')

#Resolução

#matriz = [[  ],[  ],[  ]],[[  ],[  ],[  ]],[[  ],[  ],[  ]]
#pares = 0
#soma = 0

#for i in range(0,3):
#    num = int(input(f'Digite um valor para a posição [0,{i}]: '))
#    matriz[0][i].append(num)
#    if num % 2 == 0:
#        pares += num
#    if i == 2:
#        soma += num
#for i in range(0,3):
#    num = int(input(f'Digite um valor #para a posição [1,{i}]: '))
#    matriz[1][i].append(num)
#    if num % 2 == 0:
#        pares += num
#    if i == 2:
#        soma += num
#for i in range(0,3):
#    num = int(input(f'Digite um valor #para a posição [2,{i}]: '))
#    matriz[2][i].append(num)
#    if num % 2 == 0:
#        pares += num
#    if i == 2:
#        soma += num

#print(f"{'MATRIZ 3X3':^50}")
#print(f'[{matriz[0][0][0]:^5}][{matriz#[0][1][0]:^5}][{matriz[0][2][0]:^5}]')
#print(f'[{matriz[1][0][0]:^5}][{matriz#[1][1][0]:^5}][{matriz[1][2][0]:^5}]')
#print(f'[{matriz[2][0][0]:^5}][{matriz[2][1][0]:^5}][{matriz[2][2][0]:^5}]\n')
#print(f'A soma de todos os valores pares digitados é: {pares} ')
#print(f'A soma dos valores da terceira coluna é: {soma}')
#print(f'O maior valor da segunda linha é: {max(matriz[1][0])}')


#Outra resolução (melhor)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = 0
soma_col = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
        soma_col += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print(f'A soma de todos os valores pares digitados é {soma_pares}')
print(f'A soma de todos os valores da terceira coluna é: {soma_col}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')