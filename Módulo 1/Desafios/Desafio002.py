print('Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.')

#Resolução

print('='*100)
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano,'.')

#Também é possível fazer dessa outra forma:

dia = input('coloque o dia: ')
mes = input('Coloque o mês: ')
ano = input('Coloque o ano: ')
print(f'Você nasceu no dia {dia} de {mes} de {ano}') # Também pode ser: print('Você nasceu no dia {} de {} de {}'.format(dia, mes, ano))

#Essa formatação ajuda a manter o código mais limpo e legível.

