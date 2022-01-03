print('Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.')
print('='*100)

#Resolução

cont = 1
sexo =  str(input('Insira o seu sexo[M/F]: '))
while cont == 1:
    if sexo == 'm':
        print('Você é do sexo MASCULINO')
        print ('===== FIM =====')
        cont = 0
    elif sexo == 'f':
        print('Você é do sexo FEMININO')
        print ('===== FIM =====')
        cont = 0
    else:
        sexo =  str(input('Valor inválido.\n Insira o seu sexo[M/F]: '))
        cont = 1

