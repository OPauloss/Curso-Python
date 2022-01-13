#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """Calcula o fatorial de um número. Parâmetro num determina o valor a ser calculado. Parâmetro show mostra a operação que foi feita para chegar ao resultado. Retorna o valor do fatorial de um número num"""
    if show == False:
        for i in range(num, 1, -1):
            num *= i - 1
        print(num)
    else:
        for i in range(num,1,-1):
            num *= i - 1
            print(f'{i} x ',end='')
        print(f'1 = ',end='')
        print(num)


fatorial(10)
