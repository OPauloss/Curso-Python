print('='*80)
print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
print('='*80)

#Resolução

#Caputurando a entrada do usuário
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

#Calculando
if n1 > n2 > n3:{
    print(f'Dentre os três números digitados, o maior é {n1} e o menor é {n3}')
}
if n2 > n1 > n3:{
    print(f'Dentre os três números digitados, o maior é {n2} e o menor é {n3}')
}
if n3 > n1 > n2:{
    print(f'Dentre os três números digitados, o maior é {n3} e o menor é {n2}')
}
if n1 > n3 > n2:{
    print(f'Dentre os três números digitados, o maior é {n1} e o menor é {n2}')
}
if n2 > n3 > n1:{
    print(f'Dentre os três números digitados, o maior é {n2} e o menor é {n1}')
}
if n3 > n2 > n1:{
    print(f'Dentre os três números digitados, o maior é {n3} e o menor é {n1}')
}
else:{
    print('Há números iguais na sequência!')
}

#Provavelmente há uma maneira melhor e mais rápida de fazer... rs