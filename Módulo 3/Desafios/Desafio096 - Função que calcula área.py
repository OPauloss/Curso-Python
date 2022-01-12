#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def área(a, b):
    print(f'LARGURA (m): {a}')
    print(f'COMPRIMENTO (m): {b}')
    res = a * b
    print(f'A área de um terreno {a} x {b} é de {res}m²')

    
print('Controle de Terrenos')
print('-'*30)
área(4, 50)