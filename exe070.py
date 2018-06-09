total = quant = cont = 0
nomebarato = ''
precobarato = 0
while True:
    cont += 1
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    if cont == 1:
        nomebarato = nome
        precobarato = preco
    total += preco
    if preco > 1000:
        quant += 1
    if preco < precobarato:
        nomebarato = nome
        precobarato = preco
    while True:
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if op == 'S' or op == 'N':
            break
    if op != 'S':
        break
print('=' * 10, 'FIM', '=' * 10)
print(f'''Total gasto: R${total:.2f}.
Quantidade de produtos que custam mais de RS 1000: {quant}.
({nomebarato}) é o produto mais barato, que custa Rs{precobarato:.2f}.''')
