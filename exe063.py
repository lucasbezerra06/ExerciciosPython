n = int(input('Digite um número inteiro qualquer: '))
i = 1
numAtual = int(1)
numAnt = int(0)
print(numAtual, end=', ')
while i < n:
    numProx = int(numAnt + numAtual)
    print(numProx, end=', ')
    numAnt = numAtual
    numAtual = numProx
    i += 1
print('Fim')
