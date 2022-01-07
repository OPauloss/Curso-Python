#print('''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.''')

lista = []
maior = 0
menor = 0

for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
print(f'Os itens da lista são: {lista}')
print(f'O maior item da lista é {maior} nas posições: ',end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'{pos}...', end='')
print(f'\nO menor item da lista é {menor} nas posições: ',end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos}...',end='')


   