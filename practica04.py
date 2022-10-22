# Dada una lista de temperaturas  con décimas de grado, pero sin el punto decimal para ahorrar caracteres en el almacenamiento,
# obtener la lista con el punto, usando list comprehencion.  Cuando el lector falla, se almacena un número negativo "grande".  
# Descartarlo en ese caso

temp_raw = [227, -1199, 238, 257, 218, -1199, 119]

temp = [item/10 for item in temp_raw if item > -1000]

print (temp)

# Para reemplazar el numero negativo por otro (por ejemplo 0), hacemos así:

temp_raw = [227, -1199, 238, 257, 218, -1199, 119]

temp = [item/10 if item > -1000 else 0 for item in temp_raw ]

print (temp)

# Dada una lista con enteros y strings, definir una funcion que devuelva
#  una lista que contenga solo enteros

def solo(completa):
    return [item for item in completa if type(item) != str]


completa = [99, 'no data', 95, 94, 'no data']

print ( solo(completa))