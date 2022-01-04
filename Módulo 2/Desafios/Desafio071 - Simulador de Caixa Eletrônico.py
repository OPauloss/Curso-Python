print('''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possua cédulas de R$50, R$20, R$10 e R$1.''')

print('===== Banco PH =====')


onça = 0
mico = 0
arara = 0
resp ='s'
while resp in 'sS':
    valor = int(input('Digite o valor que quer sacar: R$ '))
    onça = valor // 50
    mico = valor % 50 // 20
    arara = valor % 50 % 20 // 10
    flor = valor % 50 % 20 % 10 // 1
    print (f'Valor: R${valor}. Você receberá as seguintes cédulas:\nR$50: {onça}\nR$20: {mico}\nR$10: {arara}\nR$1: {flor}')
    resp = str(input('Quer continuar a sacar valores? [S/N]: ')).strip()
    if resp in 'Nn':
        print('Obrigado e volte sempre!')
