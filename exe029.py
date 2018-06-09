vel = float(input('Digite a velocidade do carro: '))
if vel > 80.0:
    multa = 7 * (vel - 80.0)
    print('Você foi multado em R${:.2f} por ultrapassar o limite de velociade em {}Km/h'.format(multa, (vel - 80.0)))
