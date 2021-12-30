print('='*80)
print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')
print('='*80)

#Resolução

#Capturando a entrada do usuário
num = float(input('Digite um número para saber se ele é PAR ou ÍMPAR: '))

#Calculando o valor
val = num % 2

#Declarando condições
if val == 0:{
    print('O número digitado é PAR')
}
else:{
    print('O número digitado é ÍMPAR')
}