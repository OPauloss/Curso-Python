print('='*50)
print('''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.''')
print('='*50)


num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
num = num1, num2, num3, num4
lista = sorted(num)

print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in lista:
    print(f'O primeiro valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi digitado em nenhuma posição')
print('Os números pares são: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')