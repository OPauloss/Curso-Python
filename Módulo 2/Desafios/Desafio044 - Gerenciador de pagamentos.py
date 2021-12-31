print('='*100)
print('''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
→ à vista, dinheiro/cheque: 10% de desconto
→ à vista no cartão: 5% de desconto
→ em até 2x no cartão: preço normal
→ 3x ou mais no cartão: 20% de juros. ''')
print('='*100)

#Resolução

#Capturando a entrada do usuário
preco = float(input('Qual é o preço do produto (em reais)?\n'))
pag = int(input('Selecione a forma de pagamento\n1 - À vista (dinheiro ou cheque):\n2 - À vista no cartão:\n3 - 2x no cartão\n4 - 3x ou mais no cartão\n'))

#Calculando o valor do produto e desconto/juros
if pag == 1:
    preco0 = preco - (preco * 10/100)
    print(f'Você recebeu um desconto de 10%.\nValor inicial: R${preco}\nvalor a pagar: R${preco0}')
elif pag == 2:
    preco0 = preco - (preco * 5/100)
    print(f'Você recebeu um desconto de 5%.\nValor inicial: R${preco}\nValor a pagar: R${preco0}')
elif pag == 3:
    print(f'Total a pagar: R${preco}')
else:
    preco0 = preco + (preco * 20/100)
    print(f'Com juros de 20%, o total a pagar é: {preco0}')