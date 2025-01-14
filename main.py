# IMPORTACION DE MODULOS
import os
# Menus
from modules.menus import menu_principal, sub_menu_servicios
# Mensajes de error y despedida
from modules.error_messages import adios, no_opcion, cuenta_encontrada

# Modulo 01 <- Transacciones (retirar, consignar)
import modules.transactions as t # Siempre al usar una trasaccion usamos t.(transaccion) <- si retiramos seria: t.retirar_dinero
# Modulo 02 <- Servicios
from modules.servicios import pagar_servicio_energia, pagar_servicio_gas, pagar_servicio_agua
# Importamos modulo de archivos csv
from csv import reader

# FUNCION LIMPIAR PANTALLA
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# DICCIONARIOS A USAR
cuentas = {} # Diccionario para guardar las cuentas

movimientos_archivo = [['Numero de cuenta', 'Movimiento', 'Monto', 'Nuevo Saldo', 'Fecha']]
# VARIABLES A USAR
n_cuenta = 1000 # Contador para asignar numeros unicos a las cuentas

# 1. Funcion: Crear Una Cuenta Bancaria
def crear_cuenta():

    global cuentas # Permiten modificar el diccionario declarado fuera de la funcion
    global n_cuenta # Permite modificar la variable declarada fuera de la funcion
        
    try:
        documento = int(input("Ingrese numero de documento: "))
        nombre = input("Ingrese su nombre: ")
        clave = int(input("Ingrese su clave para la cuenta: "))
    
        cuentas[n_cuenta] = { # Crea nuevos datos en el diccionario cuentas
            'DOCUMENTO': documento,
            'NOMBRE': nombre,
            'CONTRASEÑA': clave,
            'BILLETERA': 0,
            'MOVIMIENTOS': []  # Lista para guardar los movimientos
        }
        cls() # Limpia pantalla
        print(f"\n+ CUENTA CREADA CON EXITO +\n. + Numero de cuenta: {n_cuenta} +\n+ Nombre Guardado: {cuentas[n_cuenta]['NOMBRE']} +\n+ Documento: {cuentas[n_cuenta]['DOCUMENTO']} +\n")
        n_cuenta += 1 # Incrementa el numero de cuenta
    except BaseException: # Recibe error de base al tratar de operar una variable que no es un entero como entero
         print('Lo siento, Solo puedes usar numeros para tu contraseña')
         return crear_cuenta()

def info_cuenta():
    global cuentas
    while True:
        n_cuenta = input('Ingrese su numero de cuenta (o "s" para salir)> ')
        if n_cuenta.lower().strip() == "s":
            print('Cancelando..Volviendo al menu principal')
            break
        elif not n_cuenta.isdigit():
            print('Lo siento, la cuenta debe ser numerica')
            return info_cuenta()

        if int(n_cuenta) in cuentas:
            n_cuenta = int(n_cuenta)
            cuenta_encontrada(cuentas, n_cuenta)
            break
        if not n_cuenta in cuentas:
            print('Lo siento, tu cuenta no ha sido encontrada.')
# MAIN ALGORITM # ALGORITMO PRINCIPAL #
while True: # Bucle controlado
    opcion = menu_principal() # Inicializa el menu y guarda la opcion retornada en la variable #opcion#

    match opcion: # Sistema de casos para ahorrar condiciones anidadas
        case 1: # Caso 1 Creacion de la cuenta
            crear_cuenta()
        case 2:
            n_cuenta = int(input('Ingrese el numero de cuenta >'))
            monto = int(input('Ingrese el monto que deseas consignar'))
            t.consignar_dinero(n_cuenta, monto, cuentas)
        case 3:
                cuenta = input('Ingrese el numero de cuenta >')
                t.retirar_dinero(cuenta, cuentas)
        case 4:
            sub_opcion = sub_menu_servicios()
            n_cuenta = input('Ingresa tu numero de cuenta')
            match sub_opcion:
                case 1:
                    pagar_servicio_energia(cuentas, n_cuenta)
                case 2:
                    pagar_servicio_gas(cuentas, n_cuenta)
                case 3:
                    pagar_servicio_agua(cuentas, n_cuenta)
                case _:
                    print('Lo siento, servicio no encontrado')
        case 6:
            info_cuenta()
        case 7:
            adios()
            break
        case _:
            cls()
            no_opcion()