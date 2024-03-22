list_programas = []

import os 
sw = True

def fnt_agregar(p):
    global list_programas
    if p == '':
        enter = input('Debe ingresar un pograma <ENTER>')
    else:
        list_programas.append(p)
        enter = input(f'\nEl pograma {p} ha sido agregado con éxito <ENTER>')
def fnt_seleccion(op):
            if op == "1":
                program = input('Ingrese el nombre del programa: ')
                fnt_agregar(program)
            elif op == '2':
                if len(list_programas) > 0:
                    fnt_mostrar()
                else:
                    enter = input('\nNo se encontraron registros <ENTER> ')
            elif op == '3':
                fnt_eliminar()
            elif op == '4':
                pos = input('\nIngrese la posicion del pogrma a eliminar:')
                fnt_eliminar(pos)
        
def fnt_mostrar():
    print(list_programas)     
    enter = input('\n<ENTER>') 
def fnt_eliminar():
    list_programas.pop()
    enter = input('\nPrograma eliminado con éxito <ENTER>')
def fnt_eliminar(pos):
    print(list_programas,'\n')
    tamaño = len(list_programas)
    if len(list_programas) >0:
        if tamaño > int(pos):
            list_programas.pop(int(pos))
            enter = input('\nPograma eliminado con éxito <ENTER>')
        else:
            enter = input('\nPosicion no valida en la lista <ENTER>')
    else:
        enter = input('\nLa lista esta vacia <ENTER>')
while sw == True:
    os.system('cls')
    var_opcion = input(' ---- MENÚ ---- \n1. AGREGAR\n2. MOSTRAR\n3. ELIMINAR PROGRAMA X ORDERN\n4. ELIMINAR POR POSICION\n -> ')
    fnt_seleccion(var_opcion)


#Lista para programas