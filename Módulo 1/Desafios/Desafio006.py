print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')
print('='*100)

#Resolução

num = int(input('Digite um número: '))
print('O número digitado foi {}, seu dobro corresponde ao número {}, seu triplo equivale a {} e sua raiz quadrada é ou aproxima-se de {:.0f}.'.format(num, num*2, num*3, num**(1/2)))

# Formatei assim porque não quero exibir casas decimais na última operação. 