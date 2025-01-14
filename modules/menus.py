from modules.error_messages import opcion_invalida, fuera_de_rango

def menu_principal():
    print('''
++++++++++++++++++++++++++++++++++++++++++++
+           A C M E  B A N K               +
++++++++++++++++++++++++++++++++++++++++++++          
+ 1. Crear Cuenta Nueva                    +
+ 2. Consignar Dinero                      +
+ 3. Retirar Dinero                        +
+ 4. Pagar Servicios                       +
+ 5. Mostrar Movimientos Bancarios         +
+ 6. Informacion de Cuenta                 +
+ 7. Salir                                 +
++++++++++++++++++++++++++++++++++++++++++++
''')
    while True:
        opcion = input('Ingrese una opcion > ')
        # Si la entrada no es un numero
        if not opcion.isdigit(): # Verificar si la entrada contiene solo digitos
            opcion_invalida() 
            return menu_principal()
        elif int(opcion) > 7 or int(opcion) <= 0:
            fuera_de_rango()
            return menu_principal()
        return int(opcion) # Convierte la entrada a entero
    
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