'''from math import  factorial
n = int(input('Digite um número para calcular seu Fatorial::'))
f = factorial(n)
print('O fatorial de {} e {}.'.format(n, f))'''
n = int(input('Digite um número: '))
#strFat = '{}'.format(n)
i = n
fat = 1
print('{}! = '.format(n), end='')
while i > 0:
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    fat *= i
    i -= 1
    #strFat += ' X {}'.format(i)
#print('{}! = {} = {}'.format(n, strFat, fat))
print('{}'.format(fat))
