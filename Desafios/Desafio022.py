print('='*80)
print('''Crie um programa que leia nome completo de uma pessoa e mostre:
→ O nome com todas as letras maiúsculas
→ O nome com todas as letras minúsculas
→ Quantas letras ao todo (sem considerar espaços)
→ Quantas letras tem o primeiro nome.''')
print('='*80)

#Resolução

#Capturando o nome completo do usuário
nome = input('Por favor, coloque o seu nome completo: ')

#Mostrando as informações sobre o nome
print(f'O seu nome em maiúsculas é: {nome.upper()}')
print(f'O seu nome em minúsculas é: {nome.lower()}')
nome1 = nome.replace(' ', '')
print(f'O seu nome tem {len(nome1)} letras')
nlist = nome.split()
print(f'O seu primeiro nome tem {len(nlist[0])} letras')

#OBS: Utilizei o replace para retirar os espaços do nome e printei a quantidade de letras desse nome sem espaços.
#Utilizei o split para dividir o nome em vários blocos, peguei somente o primeiro o nome (índice 0) e printei a sua quantidade de letras.
