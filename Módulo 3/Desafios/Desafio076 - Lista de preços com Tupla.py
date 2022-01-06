print('='*50)
print('''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.''')
print('='*50)

prod = 'Lápis', 1.75, 'Borracha', 2.00,'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,'Compasso', 9.99,'Mochila', 120.32,'Canetas',22.30 ,'Livro', 34.90

print('-'*50)
print(f"{'TABELA DE PREÇOS':^50}")
print('-'*50)

for item in range(0, len(prod)):
    if item % 2 == 0:
        print(f'{prod[item]:.<30}', end='')
    else:
        print(f'R$ {prod[item]:>7.2f}')