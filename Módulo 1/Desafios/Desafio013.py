print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
print('='*100)

#Resultado

sal = float(input('Qual é o valor do seu salário atual? '))
sal2 = sal + sal * 15/100
print('Parabéns! Você recebeu um aumento de 15% no seu salário. Sendo assim, você, a partir de agora, receberá R$ {:.2f}'.format(sal2))