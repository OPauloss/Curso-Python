print('='*100)
print('Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.')
print('='*100)

#RESULTADO

#CAPTURANDO AS ENTRADAS DO USUÁRIO


#OPERANDO
soma = 0
for num in range(0,6):
   num = int(input('Insira o próximo número: '))
   if num % 2 == 0:
       soma = soma + num
else:
        soma = soma + 0
print(f'O resultado da soma dos números pares é: {soma}')
