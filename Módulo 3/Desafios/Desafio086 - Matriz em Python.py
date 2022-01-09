print('''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta.''')

#Resolução

#matriz = [[],[],[]],[[],[],[]],[[],[],[]]


#for n in range(0,3):
#    matriz[0][n].append(int(input(f'Digite um valor para a #posição [0,{n}]: ')))
#for n in range(0,3):
#    matriz[1][n].append(int(input(f'Digite um valor para a #posição [1,{n}]: ')))
#for n in range(0,3):
#    matriz[2][n].append(int(input(f'Digite um valor para a #posição [2,{n}]: ')))
#print(f"{'MATRIZ 3X3':^50}")
#print(f'[{matriz[0][0][0]:^5}][{matriz[0][1][0]:^5}][{matriz[0][2][0]:^5}]')
#print(f'[{matriz[1][0][0]:^5}][{matriz[1][1][0]:^5}][{matriz[1][2][0]:^5}]')
#print(f'[{matriz[2][0][0]:^5}][{matriz[2][1][0]:^5}][{matriz[2][2][0]:^5}]')

# Outra resolução

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Insira um valor para a posição [{l},{c}]: '))
print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
