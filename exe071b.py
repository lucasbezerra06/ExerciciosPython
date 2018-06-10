valor = int(input('Digite o valor a ser sacado: '))
valorSubtraido = valor
cedula = 50
totalCedula = 0
while True:
    if valorSubtraido >= cedula:
        totalCedula += 1
        valorSubtraido -= cedula
    else:
            if totalCedula > 0:
                print(f'{totalCedula} de RS{cedula}')
            if cedula == 50:
                cedula = 20
                totalCedula = 0
            elif cedula == 20:
                cedula = 10
                totalCedula = 0
            elif cedula == 10:
                cedula = 1
                totalCedula = 0
            if valorSubtraido == 0:
                break
print('-=' * 30)
print('Volte sempre, Tenha um bom dia!')

            
              