n = quant = soma = 0
n = int(input('Digite um número inteiro, digite 999 para sair: '))
while n != 999:
    soma += n
    quant += 1
    n = int(input('Digite um número inteiro, digite 999 para sair: '))
    '''n = int(input('Digite um número inteiro, digite 999 para sair: '))
    if n != 999:
        quant += 1
        soma += n'''
print('Quantidade de números digitados: {}\nSoma dos números digitados: {}'.format(quant, soma))
