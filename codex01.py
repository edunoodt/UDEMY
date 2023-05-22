from os import system
system('cls')
archivo = open ("Datos\essay.txt","r")
salida = len(archivo.read())
archivo.close()
print (salida)