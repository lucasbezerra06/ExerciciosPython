while True:
    n = int(input('Digite um número (número negativo para sair):'))
    if n < 0:
        break
    print('=-' * 20)
    for cont in range(0, 10):
        print(f'{n} X {cont} = {cont * n}')
    print('=-' * 20)
print('PROGRAMA TABUADA ENCERRADO!')

