print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.')
print('='*50)

while True:
    print('='*50)
    num = int(input(f'Quer ver a tabuada de que valor?  '))
    print('='*50)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
print('FIM DO PROGRAMA')