extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','deis','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num  = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
print(f'Você digitou no número {extenso[num]}')
