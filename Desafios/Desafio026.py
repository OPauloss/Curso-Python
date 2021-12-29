print('='*80)
print('''Faça um programa que leia uma frase pelo teclado e mostre:
→ Quantas vezes aparece a letra "A";
→ Em que posição ela aparece pela primeira vez;
→ Em que posição ela aparece pela última vez''')
print('='*80)

#Resolução

#Capturando a entrada do usuário
frase = input('Escreva uma frase para analisá-la: ')

#Quantas letras "A"?
print('Sua frase tem {} letras "A"'.format(frase.upper().count('A')))

#Em que posição aparece pela primeira vez?
print('A letra "A" aparece primeiro na posição {}'.format(frase.upper().strip().find('A')+1))

#Em que posição aparece pela última vez?
print('A Letra "A" aparece pela última vez na posição {}'.format(frase.upper().strip().rfind('A')+1))
