r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 == r3:
        triangulo = str('Equilátero')
    elif r1 != r2 != r3 != r1:
        triangulo = str('Escaleno')
    else:
        triangulo = str('Isóceles')
    print('As retas acima PODEM FORMAR um triângulo {}!'.format(triangulo))
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo!')
