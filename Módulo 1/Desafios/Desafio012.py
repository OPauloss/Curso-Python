print('Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')
print('='*100)

#Resultado

preço1 = float(input('Digite o preço do produto: '))
preço2 = preço1 - preço1 * 5/100
print('Você recebeu um desconto de 5% e agora vai pagar R${:.2f} por esse produto'.format(preço2))