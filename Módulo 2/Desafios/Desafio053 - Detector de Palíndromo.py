print('='*100)
print('Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.')
print('='*100)

#Resolução

frase1 = str(input('Digite uma frase: ')).strip().upper()
palavras = frase1.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('É palíndromo')
else:
    print('Não é palíndromo')