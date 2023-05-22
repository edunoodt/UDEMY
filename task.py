from os import system
# Programa de manejo de tareas.
def mostrar ():
    myfile = r'UDEMY\Datos\tareas.txt'
    with open (myfile,'r') as file:
        lista = file.readlines()
        
    for index, tarea in enumerate(lista):
        print (index+1, ' - ', tarea.strip('\n'))
    input('Presione enter para continuar')

def cargar():
    tarea = ''
    tareas = []
    while tarea != '***':
        system('cls')
        tarea = input ('Ingrese nueva tarea\nO "***" para salir: ')
        item = tarea +'\n'
        if tarea != '***':
            tareas.append(item.capitalize())
    myfile = r'UDEMY\Datos\tareas.txt'
    with open (myfile,"a") as archivo:
        archivo.writelines(tareas)
    


comando = ''

while comando != 's':
    system ('cls')
    print (' Ingrese letra correspondiente: \na)gregar\nm)ostrar\ne)ditar\nb)orrar\ns)alir')
    comando = input ('==>> ')
    match comando:
        case 's':
            print ('hasta la vista')
        case 'm':
            mostrar()
        
        case 'a':
            cargar()
            mostrar()

        case _:
            input('opcion incorrecta\npresione enter para continuar')