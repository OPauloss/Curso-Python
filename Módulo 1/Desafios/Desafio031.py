print('='*80)
print('Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.')
print('='*80)

#Resolução

#Capturando a entrada do usuário
dist = float(input('Qual é a distância até a localidade desejada em Km?\n'))

#Calculando os valores
if dist <= 200:{
    print('O valor total a pagar é: R${:.2f} (R$0,50 por Km)'.format(dist * 0.5))
}
else:{
    print('O valor total a pagar é: R${:.2f} (R$0.45 por Km)'.format(dist * 0.45))
}