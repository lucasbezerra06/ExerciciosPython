while True:
    cont = 0
    n = int(input('Digite um número (número negativo para sair):'))
    if n < 0:
        break
    else:
        print('=-' * 20)
        while cont <= 10:
            print(f'{cont} X {n} = {cont * n}')
            cont +=1
        print('=-' * 20)
print('FIM!')
