print('''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.''')
print('='*50)

#Resolução
somaidade = 0
homem = 0
mulher = 0
total = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo[M/F]: ')).strip().lower()[0]
    if sexo not in 'mf':
        print('OPÇÃO INVÁLIDA. CADASTRO NÃO REALIZADO.')
    elif sexo in 'MmFf':
        print('CADASTRO REALIZADO COM SUCESSO.')
        total += 1
        resp = str(input('Quer cadastrar mais um usuário? [S/N]: ')).strip().lower()[0]
    if idade >= 18:
        somaidade += 1
    if sexo == 'm':
        homem += 1
    elif sexo == 'f' and idade < 20:
        mulher += 1
    if resp not in 'Ss':
        break
print(f'''Foram cadastradas {total} pessoas, dentre as quais:
{somaidade} Atingiram a maioridade.
{homem} São homens.
{mulher} São mulheres com menos de 20 anos.''')