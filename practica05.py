# Manejo de los parametros de una función

def divide (a, b):
    return a/b


# pasando los argumentos por defecto (non keywords arguments, posicionales
print (divide (12,3))

#Pasandolos en forma expresa:
print (divide (a=12, b=4))
print (divide (a=4, b=12))

#pasandole un parámetro por defecto:

def area(a,b=4):
    return a*b

print (area(4))

# se puede alterar un parámetro pasado por defecto
print(area(4,3)) 
print(area(6))


# Cuando tenemos un número indefinido de argumentos
def promedio(*datos):
    return sum(datos)/len(datos)

print(promedio(3,6,4,1,9))


def mifuncion(*palabra):
    salida = [entrada.upper() for entrada in palabra]
    salida.sort()
    return salida

def palabras(*args):
    newpalabras=[]
    for cada in args:
        newpalabras.append(cada.upper())
        newpalabras.sort()
    return newpalabras

print(mifuncion('casa','hogar','chimenea','vivienda'))


print(palabras('casa','hogar','chimenea'))

# Cuando se tiene un número indefinido de keywords arguments
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=1,b=3,c=5))




