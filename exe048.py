soma = int(0)
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        soma += c
print('A soma entre tosos os números impares que são multiplos de três ({}) é {}'.format(count, soma))
