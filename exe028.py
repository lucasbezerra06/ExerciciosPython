from random import randint
from time import sleep
n = randint(0, 5)
print('Pensando...')
sleep(2)
num = int(input('Digite um número entre 0 e 5: '))
if num == n:
    print('Você venceu!'.format(n))
else:
    print('Você perdeu, eu pensei no número {}!'.format(n))
