print('='*80)
print('Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.')
print('='*80)

#Resolução

#Lendo a entrada do usuário
vel = float(input('Qual foi a velocidade registrada?\n'))

#Calculando o valor da multa
multa = (7 * vel) - 560

#Informando a multa ao motorista
if vel > 80:{
    print('Você foi multado por exceder o limite de velocidade. Valor total a pagar: R${:.2f}'.format(multa))
}
else:{
    print('Você está dentro do limite de velocidade estabelecido pela via. Siga em segurança.')
}

# 560 é o valor de 80 * 7