# IMPORTACION DE MODULOS
import os
from modules.menus import menu_principal, sub_menu_servicios
from modules.error_messages import adios, no_opcion
import os # Importacion modulo sistema operativo para limpiar consola

from modules.menus import menu_principal # Importamos el menu principal de nuestro modulo en: modules/menus.py
from modules.error_messages import adios, no_opcion, cuenta_inexistente # Importamos mensaje de despedida y de opcion en tramite de nuestro modulo en: modules/error_messages.py

# Modulo 01 <- Transacciones (retirar, consignar)
import modules.transactions as t # Siempre al usar una trasaccion usamos t.(transaccion) <- si retiramos seria: t.retirar_dinero

# FUNCION LIMPIAR PANTALLA
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# DICCIONARIOS A USAR
cuentas = {} # Diccionario para guardar las cuentas

# VARIABLES A USAR
n_cuenta = 1000 # Contador para asignar numeros unicos a las cuentas

# 1. Funcion: Crear Una Cuenta Bancaria
def crear_cuenta():

    global cuentas # Permiten modificar el diccionario declarado fuera de la funcion
    global n_cuenta # Permite modificar la variable declarada fuera de la funcion
        
    documento = int(input("Ingrese numero de documento: "))
    nombre = input("Ingrese su nombre: ")
    clave = int(input("Ingrese su clave para la cuenta: "))
    
    cuentas[n_cuenta] = { # Crea nuevos datos en el diccionario cuentas
        'DOCUMENTO': documento,
        'NOMBRE': nombre,
        'CONTRASEÑA': clave,
        'BILLETERA': 0
    }
    cls() # Limpia pantalla
    print(f"\n+ CUENTA CREADA CON EXITO +\n. + Numero de cuenta: {n_cuenta} +\n+ Nombre Guardado: {cuentas[n_cuenta]['NOMBRE']} +\n+ Documento: {cuentas[n_cuenta]['DOCUMENTO']} +\n")
    n_cuenta += 1 # Incrementa el numero de cuenta

def info_cuenta():
        while True:
            n_cuenta = input('Ingrese su numero de cuenta (o "s" para salir)> ')
            if n_cuenta.lower().strip() == "s":
                break
            # try execpt
            #print(f'''
#++++ CUENTA ENCONTRADA +++++=
#+ Nombre: {cuentas[n_cuenta]['NOMBRE']}
#+ Documento: {cuentas[n_cuenta]['DOCUMENTO']}
#+ Saldo: {cuentas[n_cuenta]['BILLETERA']}
#++++++++++++++++++++++++++++=
#''')
# MAIN ALGORITM # ALGORITMO PRINCIPAL #

while True: # Bucle controlado
    opcion = menu_principal() # Inicializa el menu y guarda la opcion retornada en la variable #opcion#

    match opcion: # Sistema de casos para ahorrar condiciones anidadas
        case 1: # Caso 1 Creacion de la cuenta
            crear_cuenta()
        case 3:
                cuenta = int(input('Ingrese el numero de cuenta >'))
                monto = input('Ingrese el monto que quiere retirar')
                t.retirar_dinero(cuenta, monto, cuentas)
        case 4:
            opcion = sub_menu_servicios()
            t.pagar_servicio()
        case 7:
            adios()
            break
        case _:
            cls()
            no_opcion()

# Modulos:
# Modulo gestion_billetera: Lo usaremos para manejar los retiros y las consignaciones en cada cuenta.
# La cuenta debe lucir asi: 
# #{id_cuenta: {'nombre_cliente': 'nombre', 'documento_cliente': 'documento', 'clave_cliente': 'clave'}, 'dinero_en_banco': 'DINERO'}