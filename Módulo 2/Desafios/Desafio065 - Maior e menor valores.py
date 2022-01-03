print('Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')
print('='*100)

#Resolução
laço = 0
soma = 0
cont = 1

while laço == 0:
    num = int(input('Digite um valor: '))
    maior = num
    menor = num
    resp = str(input('Quer continuar a digitar valores? ')).strip().lower()
    if resp == 's':
        laço = 1
        soma = soma + num
        cont += 1
while laço == 1 and resp != 'n':
    num = int(input('Digite outro valor: '))
    resp = str(input('Quer continuar a digitar valores? ')).strip().lower()
    if resp == 's':
        laço = 1
        soma = soma + num
        cont += 1
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    else:
        laço == 2
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        soma = soma + num
        media = soma / cont
        print(f'A média entre todos os {cont} valores digitados é: {media} ({soma} / {cont})')
        print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')
