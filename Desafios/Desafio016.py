print('='*80)
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.\nExemplo: Digite um número: 6.127\nO número 6.238 tem a parte inteira 6.')
print('='*80)

#Resolução
from math import floor

num = float(input('Digite um número para descobrir a sua parte inteira: '))
print(f'O número {num} tem a parte inteira {floor(num)}')

# Nesse exercício, importei somente a função "floor" da biblioteca "math", visto que só foi ela que eu utilizei.

# A função "math.trunc" seria mais adequada, pois ela retira as casas decimais de um número. A função "math.floor" arredonda o número para baixo (o que serve para resolver a esse exercício).
