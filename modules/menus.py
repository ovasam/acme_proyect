from modules.error_messages import invalid_option, out_of_range

def main_menu():
    print('''
++++++++++++++++++++++++++++++++++++++++++++
+           A C M E  B A N K               +
++++++++++++++++++++++++++++++++++++++++++++          
+ 1. Crear Cuenta Nueva                    +
+ 2. Informacion de Cuenta                 +
+ 3. Consignar Dinero                      +
+ 4. Retirar Dinero                        +
+ 5. Pagar Servicios                       +
+ 6. Mostrar Movimientos Bancarios         +
+ 7. Salir                                 +
++++++++++++++++++++++++++++++++++++++++++++
''')
    while True:
        opcion = input('Ingrese una opcion')
        if not opcion.isdigit():
            invalid_option()
            return main_menu()
        elif int(opcion) > 7 or int(opcion) <= 0:
            out_of_range()
            return main_menu()
        return int(opcion)