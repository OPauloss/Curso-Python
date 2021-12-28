print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')
print('='*20)

#Resolução

m = float(input('Insira aqui um valor em metros: '))
cm = m * 100
mm = m * 1000
print('{} metros equivalem a {:.0f} centímetros e {:.0f} milímetros.'.format(m, cm, mm))
