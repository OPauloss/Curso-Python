print('='*100)
print('''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. ''')
print('='*100)

#Resolução

#Coletando as informações necessárias
casa = int(input('Qual é o valor da casa que deseja comprar (em reais)?\n'))
sal = int(input('Quanto é o seu salário mensal?\n'))
prazo = int(input('Em quantos anos deseja pagar?\n'))
prest = casa / (prazo * 12)

#Calculando os valores
if prest > (30/100 * sal):
    print('''Desculpe, o seu empréstimo foi recusado porque o valor de cada prestação é maior que 30% do salário mensal
    Valor da prestação mensal: {:.2f}'''.format(prest))
else:
    print('Seu empréstimo foi aprovado. O valor de cada prestação ficará em R${:.2f} mensais.'.format(prest))