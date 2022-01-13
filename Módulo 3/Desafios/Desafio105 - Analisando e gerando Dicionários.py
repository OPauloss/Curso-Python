#'Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.'

#Resolução

def notas(*n,sit=False):
    """ Função para analisar notas de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma"""
    notas = dict()
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['média'] = sum(n) / len(n)
    if sit == True:
        if notas['média'] >= 7:
            notas['situação'] = 'Aprovado'
        elif notas['média'] < 5:
            notas['situação'] = 'Reprovado'
        else:
            notas['situação'] = 'Recuperação' 
    print('='*30)
    return notas


resp = notas(5.5,2.5,1.5)
print(resp)

