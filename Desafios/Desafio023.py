print('='*80)
print('Faça um programa que leia um número inteiro de 0 a 9999 e mostre na tela cada um dos digitos separados em unidades, dezenas, centenas e milhar')
print('='*80)

#Resolução

#Capturando a entrada do usuário:
num = int(input('Digite um número inteiro de 0 a 9999 para analisá-lo: '))
unid = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

#Mostrando as informações sobre o número:
print(f'Foram encontradas as seguintes informações sobre o número {num}:')
print(f'Unidade: {unid}\nDezena: {dez}\nCentena: {cent}\nMilhar: {mil}')