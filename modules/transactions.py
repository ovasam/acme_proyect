# IMPORTACION DE MODULOS
import os
from modules.error_messages import clave_incorrecta

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
                print("""
+++++++++++++++++++++++++++++++++++++++++++++++++
+ Por favor indique un monto valido (mayor a 0) +
+++++++++++++++++++++++++++++++++++++++++++++++++        
                      """)
            elif int(monto) > saldo:
                cls()
                print("""
+++++++++++++++++++++++++++++++++++++++++++++++++
+ No dispones del saldo suficiente en tu cuenta +
+         Intenta con un monto menor            +
+++++++++++++++++++++++++++++++++++++++++++++++++        
                      """)
            else:
                cuentas[n_cuenta]['BILLETERA'] -= int(monto)  # Restar el monto del saldo
                cls()
                print(f'''
+++++++++++++++++++++++++++++++
+      RETIRO COMPLETADO      +
+ Saldo > {cuentas[n_cuenta]['BILLETERA']}                +
++++++++++++++++++++++++++++++++
                      ''')
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
