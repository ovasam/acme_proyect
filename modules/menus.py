from modules.error_messages import opcion_invalida, fuera_de_rango

def menu_principal():
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
        opcion = input('Ingrese una opcion > ')
        if not opcion.isdigit():
            opcion_invalida()
            return menu_principal()
        elif int(opcion) > 7 or int(opcion) <= 0:
            fuera_de_rango()
            return menu_principal()
        return int(opcion)
    
def sub_menu_servicios():
    print('''
+++++++++++++++++++++++++
+        SERVICIOS      +
+++++++++++++++++++++++++
+                       +
+ 1. Energia            +
+ 2. Gas                +
+ 3. Agua               +
+ 0. Salir              +
+                       +
+++++++++++++++++++++++++++
''')
    while True:
        opcion = input('Ingrese una opcion > ')
        if not opcion.isdigit():
            opcion_invalida()
            return menu_principal()
        elif int(opcion) > 3 or int(opcion) <= 0:
            fuera_de_rango()
            return menu_principal()
        return int(opcion)