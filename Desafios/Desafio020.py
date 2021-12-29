print('='*80)
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
print('='*80)

#Resolução
import random

a1 = input('Primero aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação dos trabalhos será a seguinte:')
print(lista)

# Primeiro é necessário declarar as variáveis, colocá-las dentro de uma lista, embaralhar os elementos da lista com o comando "random.shuffle()" e depois printar o resultado.
