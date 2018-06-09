pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r
print('Progressão aritmetica de {} com razão {}'.format(pt, r))
for c in range(pt, decimo + r, r):
    print("{}".format(c), end=' -> ')
print('FIM')
