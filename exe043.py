from math import pow
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / pow(altura, 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc <= 25:
    print('Peso ideal')
elif 25 <= imc <= 30:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
