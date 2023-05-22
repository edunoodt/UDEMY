from os import system
system('cls')

"""
while True:
    try:
        total = float(input('Ingrese el monto base o total: '))
        fracción = float(input('Ingrese el monto parcial: '))

        porcentaje = fracción*100/total
        print ('\n**************************************************')
        print ('{} es el {:10.2f}% de {}'.format(fracción,porcentaje,total),'\n')
    except ValueError:
        print('\nDebe ingresar sólo números\n')
"""

with open("textos/vegetales.txt","r") as archivo:
    datos=archivo.readlines()
print(datos)