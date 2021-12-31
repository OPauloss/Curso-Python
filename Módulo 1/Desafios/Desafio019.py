print('='*80)
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.')
print('='*80)

#Resolução
import random

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
lista = [al1, al2, al3, al4]
print(f'O aluno escolhido é: {random.choice(lista)}')

# Criar listas no Python é quase que a mesma coisa que criar uma variável, a diferença é que os elementos da lista devem estar entre colchetes.