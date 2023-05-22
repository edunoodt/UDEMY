from os import system
system('cls')

archiNombres = ['Datos\marchi01','Datos\marchi02','Datos\marchi03']

for indice in archiNombres:
    archivo = open(indice, "w")
    archivo.write('Hola Mundo')
    archivo.close()