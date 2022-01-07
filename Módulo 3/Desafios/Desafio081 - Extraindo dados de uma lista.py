print('''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.''')

#Resolução

lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp not in 'Ss':
        break
lista.sort(reverse=True)
ordem = lista
print(f'Foram digitados {len(lista)} números')
print(f'Lista em ordem decrescente: {ordem}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
elif 5 not in lista:
    print('O valor 5 não faz parte da lista')
