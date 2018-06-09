km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias alugados? '))
pagar = (60 * dias) + (0.15 * km)
print('O total a paga é de R${:.2f}'.format(pagar))

