# Reescreva a função leiaInt() que fizemos no desafio104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade
# 
# #Resolução 

def leiaInt():
    while True:
        try:
            n1 = int(input('Digite um número inteiro: '))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return n1

def leiaFloat():
    while True:
        try:
            n2 = float(input('Digite um número real: '))
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            return n2

n1 = leiaInt()
n2 = leiaFloat()
print(f'Os valores digitados foram {n1} e {n2}')
