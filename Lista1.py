list_nombres = []
var_n = input('Ingrese su nombre: ')
if var_n == '':
    enter = input('Debe ingresar un nombre:')
else:
    list_nombres.append(var_n)
    enter = input(f' {var_n}, Ha sido almacenado con éxito <ENTER>')
    
print(list_nombres)