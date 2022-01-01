print('='*100)
print('''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
→ Se ele ainda vai se alistar ao serviço militar
→ Se é hora de se alistar
→ Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.  ''')
print('='*100)

#Resolução

#importando a biblioteca datetime
from datetime import date


#Capturando a entrada do usuário
ano = int(input('Digite abaixo o ano do seu nascimento\nData: '))

#Calculando a idade e informando ao usuário
idade = date.today().year - ano
if idade < 18:
    print(f'Você tem (ou terá) {idade} anos este ano. Ainda faltam {18 - idade} anos para o seu alistamento.')
elif idade == 18:
    print(f'Você tem (ou terá) {idade} anos este ano. Está na hora do seu alistamento! Vá o quanto antes à junta militar mais próxima.')
else:
    print(f'Você tem (ou terá) {idade} anos este ano. O prazo para o seu alistamento já passou! Informe-se na junta militar mais próxima.')