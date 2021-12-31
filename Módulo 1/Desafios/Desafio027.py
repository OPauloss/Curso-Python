print('='*80)
print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')
print('='*80)

#Resolução
#Capturando a entrada no usuário e dividindo o nome
nome = str(input('Por favor, digite o seu nome completo: ')).strip()
div = nome.split()

#Resolvendo o exercício
print('Seja bem-vindo, {} {}'.format(div[0],div[len(div)-1]))
