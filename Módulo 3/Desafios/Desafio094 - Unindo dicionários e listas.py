#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média. 

pessoas = dict()
lista = list()
mulheres = list()
media_maior = list()
soma_idade = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoas['sexo'] = str(input('Sexo[M/F]: ')).strip()[0]
    while pessoas['sexo'] not in 'FfMm':
        print('ERRO: Por favor, digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma_idade += pessoas['idade']
    lista.append(pessoas.copy())
    media = soma_idade / len(lista)
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas['nome'])
    esc = str(input('Quer cadastrar mais uma pessoa? [S/N]: ')).strip()[0]
    while esc not in 'SsNn':
        print('ERRO: Por favor, digite apenas S ou F.')
        esc = str(input('Quer cadastrar mais uma pessoa? [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break


print(f'Foram cadastradas: {len(lista)} pessoas.')
print(f'A média de idade do grupo é de {media} anos')
print(f'Mulheres do grupo: {mulheres}')
print(f'Pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v}')
