print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quatidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².')
print('='*100)

#Resultado

x = float(input('Qual é a largura da parede em metros? '))
y = float(input('Qual é a altura da parede em metros? '))
qtd = (x * y) / 2
print(f'São necessários {qtd} litros de tinta para pintar essa parede')