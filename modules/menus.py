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
        print("+++++++++++++++++++++++++")
        print("+        SERVICIOS      +")
        print("+++++++++++++++++++++++++")
        print("+                       +")
        print("+ 1. Energia            +")
        print("+ 2. Gas                +")
        print("+ 3. Agua               +")
        print('+ 0. Salir              +')
        print('+                       +')
        print("+++++++++++++++++++++++++++")
        opcion = int(input("¿Que desea hacer?: "))
        while opcion < 0 or opcion > 3: #Validar que la opcion esté entre 1 y 3
            opcion == int(input("Opcion invalida, eliga nuevamente"))
        return opcion
