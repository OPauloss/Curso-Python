# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

#Resolução
#nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
#media = float(input('Digite a média do aluno:'))
#print('-='*50)
#aluno = {'nome':nome, 'media':media, 'situação': ''}
#if media >= 7:
#    aluno['situação'] = 'APROVADO'
#elif media > 5 and media < 7:
#    aluno['situação'] = 'RECUPERAÇÃO'
#else:
#    aluno['situação'] = 'REPROVADO'
#print(f"O nome é {aluno['nome']}")
#print(f"A média de {aluno['nome']} é {aluno['media']}")
#print(f"Situação de {aluno['nome']}: {aluno['situação']}")

#Outra forma de fazer

aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] > 5 and aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} do aluno: {v}')

