#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se, por acaso, a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#Resolução

from datetime import date
cadastro = dict()

cadastro['Nome'] = str(input('Digite o nome do colaborador: '))
cadastro['ano'] = int(input('Digite o seu ano de nascimento [AAAA]: '))
cadastro['CTPS'] = int(input('Número da CTPS: '))
cadastro['Idade'] = date.today().year - cadastro['ano']
del cadastro['ano']


if cadastro['CTPS'] != 0:
    cadastro['Contrat'] = int(input('Digite o ano de contratação: '))
    cadastro['Salário'] = float(input('Digite seu salário: R$'))
    for k, v in cadastro.items():
        print(f'{k}: {v}')
    ano_aposent = cadastro['Contrat'] + 35
    print(f'O colaborador {cadastro["Nome"]} se aposentará em {ano_aposent} com {cadastro["Idade"] + (ano_aposent - date.today().year)} anos. Ainda faltam {ano_aposent - date.today().year} anos.')
