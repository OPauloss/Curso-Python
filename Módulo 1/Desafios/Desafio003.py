print('Crie um script Python que leia dois números e mostre a soma entre eles')
print('======================================================================')

#Resolução

n1txt = input('Insira um número: ')
n2txt = input('Insira outro número: ')
n1 = int(n1txt)
n2 = int(n2txt)
print('A soma dos números é: ', n1 + n2)

# Uma forma ainda melhor de fazer esse exercício:

n1 = int(input('Insira um número: '))
n2 = int(input('Insira um segundo número: '))
soma = n1 + n2
print(f'A soma dos números {n1} e {n2} vale {soma}')

# É possível converter o input do usuário diretamente, sem a necessidade de se criar outras variáveis para isso.

