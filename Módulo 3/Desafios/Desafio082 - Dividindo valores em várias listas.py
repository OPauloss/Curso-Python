print('Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.')

#Resolução
numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp not in 'Ss':
        break
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
print(f'Os números digitados foram: {numeros}')
print(f'Os números pares da lista são: {pares}')
print(f'Os números ímpares da lista são: {impares}')
