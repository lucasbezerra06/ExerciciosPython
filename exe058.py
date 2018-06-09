from random import randint
from time import sleep
num = 11
tentativa = 0
print('Pensando...')
sleep(1)
comp = randint(0, 10)
acertou = False
while not acertou:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 < num > 10:
        print('Numero invalido')
        print('=-' * 20)
    elif num == comp:
        print('Você venceu!')
        acertou = True
        print('=-' * 20)
        tentativa += 1
    else:
       if num < comp:
            print('Mais...Tente mas uma vez')
       elif num > comp:
           print('Menos... Tente mais uma vez')
    print('-=' * 20)
    tentativa += 1
print('Você acertou na {}º tentativa.'.format(tentativa))



