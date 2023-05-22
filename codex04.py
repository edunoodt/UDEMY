from os import system
import platform


siso = platform.system()

print (siso)

match siso:
    case 'Windows':
        system ('cls')
        print ('Windows')
    case 'Linux':
        system('clear')
        print ('Linux')
    case _:
        print ('Otro sistema')

archinombres = ['a.txt','b.txt','c.txt']

for indice in archinombres:
    ruta = 'Datos' + chr(92) + indice
    archivo = open(ruta,"r")
    print (archivo.read())
    archivo.close()
