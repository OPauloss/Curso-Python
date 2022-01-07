#print('''Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. ''')

valores = list()

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor registrado.')
    else:
        print('Número já inserido. Valor não registrado.')
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp not in 'Ss':
        break
valores.sort()
print(valores)
