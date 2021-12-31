print('='*100)
print('''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
→ Média abaixo de 5.0: REPROVADO
→ Média entre 5.0 e 6.9: RECUPERAÇÃO
→ Média 7.0 ou superior: APROVADO.''')
print('='*100)

#Resolução

#Capturando a entrada do usuário e calculando a média
n1 = float(input('Insira a nota da Prova 1: '))
n2 = float(input('Agora, insira a nota da Prova 2: '))
media = (n1 + n2) / 2

#Informando ao usuário
if media < 5:
    print('\033[0;31mREPROVADO\033[m')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('\033[0;36mAPROVADO\033[m')