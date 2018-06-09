'''from math import sqrt, pow
catOposto = float(input('Comprimento do cateto oposto: '))
catAdj = float(input('Caomprimento do cateto adjacente: '))
hip = sqrt(pow(catOposto, 2) + pow(catAdj, 2))
print('Comprimento da hipotenusa: {:.2f}'.format(hip))'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
