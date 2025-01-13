# IMPORTACION DE MODULOS
import os
from modules.error_messages import clave_incorrecta, monto_invalido, saldo_insuficiente, retiro_realizado, cuenta_inexistente

# funcion limpiar pantalla
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
        cuenta_inexistente() # Mensaje de error 'Cuenta no encontrada'
