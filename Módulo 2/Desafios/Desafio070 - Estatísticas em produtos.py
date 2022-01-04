print('''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00.
C) Qual é o nome do produto mais barato.''')

#Resolução

total = 0
caro = 0
preco = 0
menorpreco = 999999


while True:
    prod = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço do produto: R$'))
    total += preco
    if preco < menorpreco:
        menorpreco = preco
        barato = prod
    resp = str(input('Quer continuar a registrar produtos? [S/N]: '))
    if preco > 1000:
        caro += 1
    if resp not in 'Ss':
        break
print(f'O total a pagar é {total}. {caro} produtos custam mais que R$1000,00! O nome do produto mais barato é {barato}')
