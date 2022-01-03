print('''Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.''')
print('='*100)

#Resolução

cont = 0

print('========== CALCULADORA MAIOR LEGAL ==========')
num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('''[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa''')

while cont == 0:
    option = int(input('Digite a opção desejada: '))

    if option == 1:
        soma = num + num2
        print(f'A soma entre {num} e {num2} é {soma}')
        print('=================================================')
    elif option == 2:
        mult = num * num2
        print(f'Multiplicando-se os valores {num} e {num2} obtém-se {mult}')
        print('=================================================')
    elif option == 3:
        if num > num2:
            print(f'Entre os números {num} e {num2}: {num} é maior.')
            print('=================================================')
        elif num2 > num:
            print(f'Entre os números {num} e {num2}, o valor {num2} é o maior.')
            print('=================================================')
        else:
            print(f'Os valores {num} e {num2} são iguais')
            print('=================================================')
    elif option == 4:
        print('========== CALCULADORA MAIOR LEGAL ==========')
        num = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif option == 5:
        sair = str(input('Deseja mesmo sair? [S/N]: ')).strip().lower()
        if sair == 's':
            print('===== FIM DO PROGRAMA =====')
            cont = 1
        else:
            print('========== CALCULADORA MAIOR LEGAL ==========')
            num = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
