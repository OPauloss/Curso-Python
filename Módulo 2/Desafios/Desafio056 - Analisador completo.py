print('='*100)
print('''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
→ A média de idade do grupo.
→ Qual é o nome do homem mais velho.
→ Quantas mulheres têm menos de 20 anos.''')
print('='*100)

#Resolução
cont = 0
soma = 0
h = 0
novoh = ''
for i in range(0,4):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M / F): '))
    
#Condições
    if idade > 0:
        soma = soma + idade
    if idade < 20 and sexo.lower() == 'f':
        cont = cont + 1
    if sexo == 'm' and idade > h :
        h = (idade - h) + h
        novoh = nome

#Informando ao usuário  
print(f'Existem {cont} mulheres com menos de 20 anos no grupo.')
print(f'A média de idade do grupo é {soma / 4:.1f} anos')
print(f'O homem mais velho se chama {novoh} e tem {h} anos')

#"Elif" só funciona dentro da mesma ramificação de "if"

#Resumo dos dados
