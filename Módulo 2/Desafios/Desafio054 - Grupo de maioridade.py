print('='*100)
print('Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores')
print('='*100)

from datetime import date

cont = 0
cont2 = 0
for i in range(0, 7):
    ano = int(input(f'Coloque ano de nascimento da {i + 1}ª pessoa: ').strip())
    if date.today().year - ano >= 18:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print(f'{cont} pessoas da lista atingiram a maioridade.')
print(f'{cont2} pessoas da lista não atingiram a maioridade')

