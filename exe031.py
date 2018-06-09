dis = float(input('Digite a distância da viagem: '))
'''if dis > 200:
    pas = dis * 0.45
else:
    pas = dis * 0.50'''
pas = dis * 0.50 if dis <= 200 else dis * 0.45
print('O preço da passagem é de R${:.2f}, por percorrer {}Km'.format(pas, dis))
