nombre = input ('ingrese su nombre: ')
apellido = input ('ingrese su apellido: ')
nacim = input ('Fecha de nacimiento: ')



print ('Señor %s %s, usted nació el %s' % (nombre, apellido, nacim))

calle = input('Calle: ')
numero = input('Numero: ')
ciudad = input ('Ciudad: ')

print (f'Señor {apellido}, usted vive en {calle} nro {numero}, ciudad de {ciudad}')

# Otra manera de darle forma al string:

print ('Señor {}, usted vive en {} nro {}, ciudad de {}'.format(apellido, calle, numero, ciudad))
