print('Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.')
print('='*100)

#Resolução
num = int(input('Digite o primeiro número da PA: '))
raz = int(input('Insira a razão da PA: '))
print(num)
cont = 1
resp = ''

while cont < 10:
    num = num + raz
    cont += 1
    print(num)
    if cont == 10:
        resp = str(input('Deseja continuar a ver os próximos termos da PA? [S/N]: ')).strip().lower()
        if resp == 's':
            termos = int(input('Quantos mais termos deseja visualizar? '))
            cont = (cont - termos)
            resp = ''
        else:
            print('===== FIM DO PROGRAMA =====')