preco = float(input('Digite o preço do produto: R$'))
novo = preco - (preco * 5 / 100)
print('O novo preço do produto é R${:.2f}'.format(novo))
