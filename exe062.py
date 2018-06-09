pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
quant = 10
print('Progresão aritmetica de {} com razão {}'.format(pt, r))
termo = pt
while quant != 0:
    if cont <= quant:
        print('{}'.format(termo), end=' -> ')
        termo += r
        cont += 1
    else:
        print('FIM')
        print('-=' * 30)
        quant = int(input('Quantos termos a mais você deseja exibir? '))
        cont = 1
print('Fim do programa!')
