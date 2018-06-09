nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('Primeiro nome {}.'.format(div[0]))
print('Seu ultimo nome {}.'.format(div[len(div) - 1]))
