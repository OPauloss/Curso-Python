# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

#Resolução


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos, o voto é OPCIONAL'
    else:
        return f'Com {idade} anos, NÃO VOTA.' 


ano = int(input('Digite o ano de nascimento: [MMMM]: '))
print(voto(ano))



