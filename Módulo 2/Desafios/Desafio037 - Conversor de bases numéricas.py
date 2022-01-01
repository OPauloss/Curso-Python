print('='*100)
print('''Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
→ 1 para binário
→ 2 para octal
→ 3 para hexadecimal''')
print('='*100)

#Capturando a entrada do usuário e fornecendo as opções:
num = int(input('Digite um número inteiro: '))
opcao = int(input('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL\n'''))
print(f'Sua opção: {opcao}')

#Convertendo valores
if opcao == 1:
    print(f'{num} para BINÁRIO: {num:b}')
elif opcao == 2:
    print(f'{num} para OCTAL: {num:o}')
elif opcao == 3:
    print(f'{num} para HEXADECIMAL: {num:x}')
else:
    print('Opção inválida')

# :b para binário, :o para octal, :x para hexadecimal (minúsculas), :X para hexadecimal (maiúsculas).