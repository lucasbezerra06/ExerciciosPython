maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('-=' * 20)
print('O maior peso foi de {}Kg.'.format(maior))
print('O menor peso foi de {}Kg.'.format(menor))
