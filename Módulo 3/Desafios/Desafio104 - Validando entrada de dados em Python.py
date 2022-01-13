# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n')

def leiaInt(i):
    n = str(input(i)).strip()
    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um número inteiro!')
        n = str(input('\033[mDigite um número: ')).strip()
    return int(n)
        



n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')