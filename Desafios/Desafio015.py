print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
print('='*100)

#Resultado
dias = int(input('Por quantos dias o carro foi alugado?\n'))
km = float(input('Quantos km foram rodados?\n'))
val = (dias * 60) + (km * 0.15)
print('O valor total a ser pago é de R${:.2f}'.format(val))