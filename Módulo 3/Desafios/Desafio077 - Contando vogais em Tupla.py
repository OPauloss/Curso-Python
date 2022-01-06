print('='*50)
print('''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.''')
print('='*50)

palavras = ['oi','ola','tudo','bem','tchau','volte sempre','ate','como','vai','bolo','creme','avalanche']



for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# Cada item dentro da tupla é uma lista!!! Por isso, podemos seccionar a variável até atingir o único caracter que sobrar.
