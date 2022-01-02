print('='*100)
print('Refaça o Desafio009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for')
print('='*100)

#RESOLUÇÃO

num = int(input('Insira um número para conhecer sua tabuada: '))

print(f'======= Tabuada do {num} =========')
for num2 in range(0,11):
    result = num * num2
    print(f'{num} x {num2} = {result}')
print('========== FIM ============')