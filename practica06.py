"""
mi_arch = open ('textos/fruits.txt')
print (mi_arch.read())
mi_arch.close()


with open('textos/fruits.txt') as mi_arch:
    print(mi_arch.read())

"""
entrada = ''
cadena = ''
while entrada != 'xxx':
    entrada=input('Ingrese vegetal (xxx para salir): ')
    if entrada != 'xxx':
        cadena += entrada + '\n'

with open('textos/vegetales.txt',"w") as mi_arch:
    mi_arch.write(cadena)

    mi_arch.write('manzana')

