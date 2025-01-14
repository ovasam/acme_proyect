# IMPORTACION DE MODULOS
import os
from modules.error_messages import clave_incorrecta, monto_invalido, saldo_insuficiente, retiro_realizado, cuenta_inexistente

# funcion limpiar pantalla
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def pagar_servicio(n_cuenta, cuentas, opcion):
    #Parámetros:
    #n_cuenta (int): Número de la cuenta desde la cual se quiere pagar.
    #cuentas (dict): Diccionario que contiene las cuentas y sus datos.

    # Verificar si la cuenta existe
    if n_cuenta in cuentas:
        # Solicitar clave del usuario
        password = int(input("Ingrese su clave: "))
        if password == str(cuentas[n_cuenta]['CONTRASEÑA']):
            saldo_actual = cuentas[n_cuenta]['BILLETERA']

            # Seleccionar servicio
            servicio_seleccionado = input("Ingrese el nombre del servicio que desea pagar: ")
            if servicio_seleccionado == '' :
                monto = SERVICIOS[servicio_seleccionado]

                # Validar si hay saldo suficiente
                if monto > saldo_actual:
                    cls()
                    saldo_insuficiente()  # Saldo insuficiente
                else:
                    # Descontar el saldo
                    cuentas[n_cuenta]['BILLETERA'] -= monto
                    cls()
                    pago_realizado(servicio_seleccionado, monto, cuentas, n_cuenta)  # Mensaje de éxito
            else:
                cls()
                print("Error: Servicio no encontrado.")
        else:
            cls()
            clave_incorrecta()  # Clave incorrecta
    else:
        cls()
        cuenta_inexistente()  # Cuenta inexistente

# 4. Función: Retirar Dinero
def retirar_dinero(n_cuenta, monto, cuentas):
    
    #Parámetros:
    #id_cuenta (int): Número de la cuenta desde la que se quiere retirar.
    #monto (float): Monto de dinero a retirar.
    #cuentas (dict): Diccionario con las cuentas y sus datos.

    #Verificar si la cuenta existe en el diccionario de cuentas
    if n_cuenta in cuentas:
        password = input("Ingrese su clave: ")
        if int(password) == cuentas[n_cuenta]['CONTRASEÑA']:
            saldo = cuentas[n_cuenta]['BILLETERA'] # 0
            # Verificar si hay suficiente saldo para realizar el retiro
            if int(monto) <= 0:
                cls()
                monto_invalido() # Mensaje de error 'Monto mayor a 0'
            elif int(monto) > saldo:
                cls()
                saldo_insuficiente() # Mensaje de error 'Monto insuficiente'
            else:
                cuentas[n_cuenta]['BILLETERA'] -= int(monto)  # Restar el monto del saldo
                cls()
                retiro_realizado(cuentas, n_cuenta) # Mensaje de exito, 'Retiro Realizado.'
        else:
            cls()
            clave_incorrecta()
    else:
        cls()
        print("""
+++++++++++++++++++++++++++++++++
+  Error: La cuenta no existe.  +
+++++++++++++++++++++++++++++++++
              """)
