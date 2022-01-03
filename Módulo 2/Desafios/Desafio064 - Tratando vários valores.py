print('Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).')
print('='*100)

#Resolução

cont = 0
soma = 0
digit = 0
while cont == 0:
    num = int(input('Digite um número [999 para parar]: '))
    soma = soma + num
    digit += 1
    if num == 999:
        cont = 1
        digit -= 1
        print(f'A soma dos números digitados foi: {soma - 999}. Foram digitados {digit} valores.')
        print('FIM')

