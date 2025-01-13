# IMPORTACION DE MODULOS
from modules.menus import main_menu
from modules.error_messages import good_bye

# DICCIONARIOS A USAR
cuentas = {} # Diccionario para guardar las cuentas

# VARIABLES A USAR
n_cuenta = 1000

# 1. Funcion: Crear Una Cuenta Bancaria
def crear_cuenta():
    
    global cuentas
    global n_cuenta
    
    #Datos del usuario
    
    cc = int(input("Ingrese numero de documento: "))
    name = input("Ingrese su nombre: ")
    password = int(input("Ingrese su clave para la cuenta: "))
    
    cuentas[n_cuenta] = {
        'DOCUMENTO': cc,
        'NOMBRE': name,
        'CONTRASEÑA': password
    }
    n_cuenta += 1
    print(cuentas)

# 4. Funcion: Pagar servicios    

def pagar_servicios():
    def menu2():
        print("===============")
        print("===Servicios===")
        print("===============")
        print(" ")
        print("1. Energia")
        print("2. Luz")
        print("3. Agua")
        opcion = int(input("¿Que desea hacer?: "))
        while opcion < 1 or opcion > 3: #Validar que la opcion esté entre 1 y 3
            opcion == int(input("Opcion invalida, eliga nuevamente"))
        return opcion

# 5. Funcion: Mostrar Movimientos Bancarios    
def movimientos_bancarios():
    print()


# MAIN ALGORITM # ALGORITMO PRINCIPAL #
while True: # Bucle controlado
    opcion = main_menu() # Inicializa el menu y guarda la opcion retornada en la variable #opcion#

    match opcion: # Sistema de casos para ahorrar condiciones anidadas
        case 1: # Caso 1 Creacion de la cuenta
            crear_cuenta()
            print(f'\n+ CUENTA CREADA CON EXITO +\n. + Numero de cuenta: {1000} +\n+ Nombre Guardado: {cuentas[1000]['NOMBRE']} +\n+ Documento: {cuentas[1000]['DOCUMENTO']} +\n')
        case 7:
            good_bye()
            break
        case _:
            print('OPCION NO IMPLEMENTADA. LO SIENTO')


# Modulos:
# Modulo gestion_billetera: Lo usaremos para manejar los retiros y las consignaciones en cada cuenta.
# La cuenta debe lucir asi: 
# #{id_cuenta: {'nombre_cliente': 'nombre', 'documento_cliente': 'documento', 'clave_cliente': 'clave'}, 'dinero_en_banco': 'DINERO'}