print('='*80)
print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
print('='*80)

#Resolução

#Capturando a entrada do usuário
ano = int(input('Digite o ano para saber se é bissexto: '))

#Qualquer ano que seja divisível por 4 é um ano bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:{
    print(f'O ano {ano} é bissexto')
}
else:{
    print(f'O ano {ano} não é bissexto.')
}