print('Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while')
print('='*100)

#Resolução
num = int(input('Digite o primeiro número da PA: '))
raz = int(input('Insira a razão da PA: '))
print(num)
cont = 1

while cont < 10:
    num = num + raz
    cont += 1
    print(num)