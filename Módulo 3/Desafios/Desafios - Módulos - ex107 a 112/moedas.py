def metade(p,form = False):
    p /= 2
    if form == True:
        p = f'R${p:.2f}'
        p.replace('.',',')
    return p


def dobro(p, form = False):
    p *= 2
    if form == True:
        p = f'R${p:.2f}'
        p.replace('.',',')
    return p


def aumentar(p,num,form=False):
    p += (num/100 * p)
    if form == True:
        p = f'R${p:.2f}'
        p.replace('.',',')
    return p


def diminuir(p,num,form=False):
    p -= (num/100 * p)
    if form == True:
        p = f'R${p:.2f}'
        p.replace('.',',')
    return p


def moeda(num):
    num = f'R${num:.2f}'
    return num.replace('.',',')


def resumo(p, aum, dim):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \tR${p:.2f}')
    print(f'Dobro do preço: \tR${p*2:.2f}')
    print(f'Metade do preço: \tR${p/2:.2f}')
    print(f'{aum}% de aumento: \tR${p + p * (aum/100):.2f}')
    print(f'{dim}% de redução: \tR${p - p * (dim/100):.2f}')
    print('-'*30)
