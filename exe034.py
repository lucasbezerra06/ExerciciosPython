salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250.00:
    aumento = 10
else:
    aumento = 15
novo = salario + salario * (aumento / 100)
print('O seu aumento foi de {:.0f}%, e seu novo salario é R${:.2f}'.format(aumento, novo))
