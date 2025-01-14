# IMPORTACION DE MODULOS
import os
from csv import writer
from modules.error_messages import clave_incorrecta, monto_invalido, saldo_insuficiente, retiro_realizado, cuenta_inexistente
from datetime import date, time, datetime
# funcion limpiar pantalla
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# 3. Función: Consignar Dinero
def consignar_dinero(n_cuenta, monto, cuentas):
    fecha = datetime.now()
    #Parámetros:
    #n_cuenta (int): Número de la cuenta donde se quiere consignar.
    #monto (float): Monto de dinero a consignar.
    #cuentas (dict): Diccionario con las cuentas y sus datos.

    # Verificar si la cuenta existe en el diccionario de cuentas
    if n_cuenta in cuentas:
        password = input("Ingrese su clave: ")
        if int(password) == cuentas[n_cuenta]['CONTRASEÑA']:
            # Verificar que el monto sea válido
            if int(monto) <= 0:
                cls()
                monto_invalido()  # Mensaje de error 'Monto mayor a 0'
            else:
                cuentas[n_cuenta]['BILLETERA'] += int(monto)  # Sumar el monto al saldo
                #Guardar el movimiento en un archivo CSV
                with open('movimientos_bancarios.csv', 'a', newline='') as file:
                    escritor = writer(file)
                    escritor.writerow([n_cuenta, 'Consignacion', monto, cuentas[n_cuenta]['BILLETERA'], f'{fecha.strftime('%d - %m - %Y')}'])
                cls()
                print(f"""
+++++++++++++++++++++++++++++++++
+ Consignación exitosa.         +
+ Nuevo saldo: {cuentas[n_cuenta]['BILLETERA']}          +
+++++++++++++++++++++++++++++++++
                """)
                movimiento = ['Consignacion', 'Dia/mes/year', f'Monto: {monto}', f'Saldo: {cuentas[n_cuenta]['BILLETERA']}']
                cuentas[n_cuenta]['MOVIMIENTOS'].append(movimiento)
                print(cuentas[n_cuenta])
        else:
            cls()
            clave_incorrecta()  # Mensaje de error 'Clave incorrecta'
    else:
        cls()
        cuenta_inexistente()

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
                 # Guardar el movimiento directamente en el archivo CSV
                with open('movimientos_bancarios.csv', 'a', newline='') as file:
                    escritor = writer(file)
                    escritor.writerow([n_cuenta, 'Retiro', monto, cuentas[n_cuenta]['BILLETERA']])
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
        
# 5. Función: pagar_servicio
def pagar_servicio(n_cuenta, cuentas, opcion):
    #Parámetros:
    #n_cuenta (int): Número de la cuenta desde la cual se quiere pagar.
    #cuentas (dict): Diccionario que contiene las cuentas y sus datos.

    # Verificar si la cuenta existe
    if n_cuenta in cuentas:
        # Solicitar clave del usuario
        password = int(input("Ingrese su clave: "))
        if password == cuentas[n_cuenta]['CONTRASEÑA']:
            saldo_actual = cuentas[n_cuenta]['BILLETERA']
            
            print(f'TU SALDO ACTUAL = {saldo_actual}')
            
            # Seleccionar servicio
            match opcion:
                case 1:
                    print('Servicio de Luz')
                case 2:
                    print('Servicio de Gas')
                case 3:
                    print('Servicio de Agua')
                    
            if saldo_actual > 0:
                # Escribir el pago en el archivo CSV
                with open('movimientos_bancarios.csv', 'a', newline='') as file:
                    escritor = writer(file)
                    escritor.writerow([n_cuenta, f'Pago Servicio {opcion}', saldo_actual, 0])
                cuentas[n_cuenta]['BILLETERA'] = 0
                cls()
                print(f"Servicio {opcion} pagado con éxito.")
            else:
                cls()
                saldo_insuficiente()
        else:
            cls()
            clave_incorrecta()  # Clave incorrecta
    else:
        cls()
        cuenta_inexistente()  # Cuenta inexistente


