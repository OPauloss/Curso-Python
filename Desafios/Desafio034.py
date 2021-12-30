print('='*80)
print('''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.''')
print('='*80)

#Resolução

#Entrada do usuário
sal = float(input('Qual é o seu salário atual?\n'))

#Calculando o aumento
if sal <= 1250:{
    print(f'Você recebeu um aumento de 15%. Seu novo salário é R${sal + (sal * 15/100)}')
}
else:{
    print(f'Você recebeu um aumento de 10%. Seu novo salário é R${sal + (sal * 10/100)}')
}