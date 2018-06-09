from random import randint
from time import sleep
op = int(input('''1 - pedra
2 - papel
3 - tesoura: '''))
jokenpo = ('Pedra', 'Papel', 'Tesoura')
oppc = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if 0 > op > 3:
    print('opção invalida')
else:
    print('-='*10)
    print('{} X {}'.format(jokenpo[op-1], jokenpo[oppc-1]))
    print('-='*10)

    if op == oppc:
        print('Empate')
    elif op-oppc == (-2) or op-oppc == 1:
        print('Você venceu!')
    else:
        print('Você perdeu!')
