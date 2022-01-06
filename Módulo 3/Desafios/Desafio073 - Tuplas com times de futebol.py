print('='*50)
print('''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.''')
print('='*50)

#Resolução

times = 'Atletico-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','America-MG','Atletico-GO','Santos','Ceara SC','Internacional','Sao Paulo','Athletico-PR','Cuiaba','Juventude','Gremio','Bahia','Sport Recife','Chapecoense'
chap = times.index('Chapecoense') + 1


print(f'Os cinco primeiros times do Campeonato são: {times[:5]}')
print(f'Os últimos quatro colocados da tabela são: {times[-4:]}')
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print(f'O time do Chapecoense está na {chap}ª posição')