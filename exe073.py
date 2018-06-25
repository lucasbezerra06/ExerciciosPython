tabela = ('Flamengo','Atlético Mineiro','São Paulo','Internacional','Grêmio','Palmeiras','Sport Recife','Cruzeiro','Botafogo','Corinthians','Vasco','Fluminense','America-mg','Chapecoense','Santos','Vitória','Bahia','Paraná','Atlético-pr','Ceará')
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[-5:]}')
print(f'Times em ordem alfabética{sorted(tabela)}')
chapeco = tabela.index('Chapecoense' ) + 1
print(f'Posição da chapecoense é: {chapeco}')