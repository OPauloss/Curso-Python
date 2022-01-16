# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

#Resolução
import moedas

p = float(input('Digite o preço: R$'))
#print(f'A medade de {moedas.moeda(p)} #é {moedas.metade(p,True)}')
#print(f'O dobro de {moedas.moeda(p)} #é {moedas.dobro(p,True)}')
#print(f'Aumentando 10%, temos {moedas.#aumentar(p,10,True)}')
#print(f'Reduzindo 13%, temos {moedas.#diminuir(p,13,True)}')
print(moedas.resumo(p,50,25))