n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if cont == 2:
    print('\nO número {} é primo'.format(n))
else:
    print('\nO número {} não é primo'.format(n))