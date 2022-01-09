#print('''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.''')

pessoas = list()
dado = list()
peso = list()

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    peso.append(dado[1])
    dado.clear()
    esc = str(input('Continuar? [s/n]: ')).strip()[0]
    if esc not in 'Ss':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
peso.sort()
print(f'O maior peso é {peso[-1]}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == peso[-1]:
        print(f'{p[0]}...', end=' ')
print(f'\nO menor peso é {peso[0]}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == peso[0]:
        print(f'{p[0]}...', end=' ')
