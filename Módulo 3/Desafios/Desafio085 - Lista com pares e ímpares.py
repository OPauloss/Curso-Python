print('Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.')

#Resolução

#valores = []
#pares = []
#impares = []

#for val in range(0,7):
#    valores.append(int(input('Digite um valor: ')))
#for num in range(0,7):
#    if valores[num] % 2 == 0:
#        pares.append(valores[num])
#    if valores[num] % 2 != 0:
#        impares.append(valores[num])

#print(f'Os números digitados foram: {valores}')
#print(f'Os valores pares, em ordem crescente, são: {sorted(pares)#}')
#print(f'Os valores ímpares, em ordem crescente, são {sorted#(impares)}')

numeros = [[],[]]

for i in range(0,7):
    valor = int(input(f'Digite um valor para a posição {i}: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 != 0:
        numeros[1].append(valor)
print(f'Os valores pares são {sorted(numeros[0])}')
print(f'Os valores ímpares são {sorted(numeros[1])}')
