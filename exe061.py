pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
print('Progresssão aritmetica de {} com razão {}'.format(pt, r))
cont = 1
while cont <= 10:
    print('{}'.format(pt), end=' -> ')
    pt += r
    cont += 1
print('FIM')
