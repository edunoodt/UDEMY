from os import system
system('cls')

nuevo = input('por favor ingrese un nuevo miembro: ')
archivo = open ("Datos\members.txt","a")
archivo.write(nuevo+'\n')
archivo.close()
archivo = open ("Datos\members.txt","r")
salida= archivo.read()
archivo.close()
print (salida)
