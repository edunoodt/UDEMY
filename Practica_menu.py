from os import system as sy

def primero():
    return 'primero'

def segundo():
    return 'segundo'

def tercero():
    return 'tercero'

menu = [primero, segundo, tercero]

ingreso = ''
while ingreso != 4:
    sy('clear')
    print ('Ingrese 1, 2, 3  ó 4 para salir')
    ingreso = int (input('==>> '))
    if ingreso != 4: 
        print (menu[ingreso-1]())
        input('enter para continuar')


