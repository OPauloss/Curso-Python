print('='*80)
print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.')
print('='*80)

#Resolução

#Capturando a entrada do usuário e procurando pela string 'Silva'
nome = input('Qual é o seu nome completo?\n').strip().lower()
nome1 = nome.find('silva')

if(nome1 == -1):{
    print('Você não tem Silva no nome')}
else:{
    print('Você tem Silva no nome')}
