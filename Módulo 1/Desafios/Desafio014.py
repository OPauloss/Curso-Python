print('Escreva um programa que converta uma temperatura digitada em ºC e converta-a para ºF.')
print('='*100)

########### Resolução ##########
cels = float(input('Qual é a temperatura atual em Celsius (ºC)?\n'))
faren = (cels * 9/5) + 32
print(f'{cels}ºC equivale a {faren}ºF')

# Essa fórmula é facilmente encontrada na internet. 
#Obs: O comando "\n" faz com que se quebre uma linha.