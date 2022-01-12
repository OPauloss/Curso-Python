# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Resolução

def escreva(msg):
    print(f"{'~' * len(msg):^40}")
    print(f'{msg:^40}')
    print(f"{'~' * len(msg):^40}")


escreva('oi!')
