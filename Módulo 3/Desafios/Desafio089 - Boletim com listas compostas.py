print('Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.')

#Resolução
lista = []
lista2 = []
alunos = []
notas =  []
medias = []

while True:
    # Cadastrando o aluno
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    lista.append(nome)
    lista2.append(n1)
    lista2.append(n2)
    alunos.append(lista[0])
    notas.append(lista2[:])
    medias.append(media)
    lista.clear()
    lista2.clear()
    # Interrompendo o loop
    esc = str(input('Quer cadastrar outro aluno? [s/n]: ')).strip()[0]
    if esc in 'Nn':
        break
#Boletim
print(f'='*60)
print(f'{"Nº":<4} {"ALUNO":<10}{"MÉDIA":>8}')
print(f'='*60)
for i,a in enumerate(alunos):
    print(f'{i:<4}{alunos[i]:<10}{medias[i]:>8}')
while True:
    resp = int(input('Quero ver as notas individuais de: [Nº do aluno (999 para sair)]: '))
    if resp == 999:
        print('FIM')
        break
    if resp in range(0,len(alunos)):
        print(f'Notas de {alunos[resp]}: {notas[resp]}')
