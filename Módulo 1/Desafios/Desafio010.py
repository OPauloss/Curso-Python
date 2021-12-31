print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')
print('='*100)

#Resolução

real = float(input('Quanto dinheiro você tem em reais? '))
dolar = real / 5.63
print('Com R$ {:.2f} você pode comprar USD {:.2f}'.format(real, dolar))

# Valor de 1 USD em 28 de dezembro de 2021 é de 5,63 BRL