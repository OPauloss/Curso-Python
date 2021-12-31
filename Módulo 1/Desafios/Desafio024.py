print('='*80)
print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".')
print('='*80)

#Resolução

cep = input('Qual é o nome da sua cidade?\n')
cep1 = cep.strip().lower().split()

if(cep1[0] == 'santo'):{
    print('O nome da sua cidade começa com Santo no nome')}
else:{
    print('O nome da sua cidade não começa com Santo no nome')}

#Essa não foi a solução ensinada na aula 09, mas foi como consegui resolver baseado nos meus conhecimentos anteriores.