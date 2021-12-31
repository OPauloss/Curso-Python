print('='*100)
print('''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
→ Abaixo de 18.5: Abaixo do peso
→ Entre 18.5 e 25 Peso ideal
→ 25 até 30: Sobrepeso
→ 30 até 40: Obesidade
→ Acima de 40: Obesidade mórbida''')
print('='*100)

#Resolução

#Capturando a entrada do usuário
peso = float(input('Insira a sua peso: '))
altura = float(input('Insira o seu altura: '))

#Calculando o IMC e informando ao usuário
imc = peso / (altura * altura)
if imc < 18.5:
    print('ABAIXO DO PESO: IMC:{:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL: IMC: {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('SOBREPESO: IMC: {:.1f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('OBESIDADE: IMC: {:.1f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA: IMC: {imc}')