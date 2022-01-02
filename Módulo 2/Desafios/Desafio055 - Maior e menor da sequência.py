print('='*100)
print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.')
print('='*100)

#Resolução

#Declarando acumuladores
pesog = 0
pesop = 0
for i in range(0,5):
    peso = float(input('Digite o seu peso: '))
    if i == 0: 
        pesog = peso
        pesop = peso
    else:
        if peso > pesog:
            pesog = peso
        if peso < pesop:
            pesop = peso
print(f'O maior peso registrado foi {pesog:.1f}Kg')
print(f'O menor peso registrado foi {pesop:.1f}Kg')