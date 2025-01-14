# IMPORTACION DE MODULOS
import os
from csv import writer
from modules.error_messages import clave_incorrecta, monto_invalido, saldo_insuficiente, retiro_realizado, cuenta_inexistente, consignacion_exitosa, monto_numerico
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
            # Verificar que el monto sea válido
            if int(monto) <= 0:
                cls()
                monto_invalido()  # Mensaje de error 'Monto mayor a 0'
            
            cuentas[n_cuenta]['BILLETERA'] += int(monto)  # Sumar el monto al saldo
            #Guardar el movimiento en un archivo CSV
            with open('movimientos_bancarios.csv', 'a', newline='') as file:
                escritor = writer(file)
                if file.tell() == 0:  # Si el archivo está vacío
                    escritor.writerow(["  Numero de cuenta  ", "  Tipo de movimiento  ", "  Monto Movido  ", "  Saldo Actual  ", "  dia/mes/año :hora  "])  # Encabezados
                escritor.writerow([f'{n_cuenta}', ' Consignacion ', f' {monto} ', f' {cuentas[n_cuenta]["BILLETERA"]} ', f' {fecha.strftime("%d/%m/%Y %H:%M")} '])
            cls()
            consignacion_exitosa(cuentas, n_cuenta)
            movimiento = ['Consignacion',  f'{fecha.strftime("%d/%m/%Y %H:%M")}', f'Monto: {monto}', f'{cuentas[n_cuenta]["BILLETERA"]}']
            cuentas[n_cuenta]['MOVIMIENTOS'].append(movimiento)
            print(cuentas[n_cuenta])
    else:
        cls()
        cuenta_inexistente()

# 4. Función: Retirar Dinero
def retirar_dinero(n_cuenta, cuentas): # (n_cuenta(str) = numero de cuenta), (monto(int) = monto para retirar), (cuentas(dict) = diccionario de cuentas)
    fecha = datetime.now()
    if not n_cuenta.isdigit():
        monto_numerico()
        return
    n_cuenta = int(n_cuenta)
    #Verificar si la cuenta existe en el diccionario de cuentas
    try:
        if n_cuenta in cuentas:
            
            password = int(input("Ingrese su clave: "))
            if password != cuentas[n_cuenta]['CONTRASEÑA']:
                cls()
                clave_incorrecta()
                n_cuenta = str(n_cuenta)
                return

            saldo = cuentas[n_cuenta]['BILLETERA'] # 0
            monto = int(input('Ingrese el monto que desea retirar >'))
            
            if saldo < monto:
                cls()
                saldo_insuficiente() # Mensaje de error 'Monto mayor a 0'
                n_cuenta = str(n_cuenta)
                return
            
            elif monto <= 0:
                print('Indique un saldo mayor a 0 para retirar')
                # Guardar el movimiento directamente en el archivo CSV
            
            cuentas[n_cuenta]['BILLETERA'] -= int(monto)

            with open('movimientos_bancarios.csv', 'a', newline='') as file:
                escritor = writer(file)
                if file.tell() == 0:  # Si la linea a la que tell apunta esta vacia
                    escritor.writerow(["  Numero de cuenta  ", "  Tipo de movimiento  ", "  Monto Movido  ", "  Saldo Actual  ", "  dia/mes/año :hora  "])  # Encabezados
                    escritor.writerow([f'{n_cuenta}', ' Consignacion ', f' {monto} ', f' {cuentas[n_cuenta]["BILLETERA"]} ', f' {fecha.strftime("%d/%m/%Y %H:%M")} '])
                    cls()
                retiro_realizado(cuentas, n_cuenta) # Mensaje de exito, 'Retiro Realizado.'
                
        else:
            cls()
            print("""
+++++++++++++++++++++++++++++++++
+  Error: La cuenta no existe.  +
+++++++++++++++++++++++++++++++++
            """)
    except BaseException as e:
        print('Error: Usaste un dato incorrecto, Verifica tus datos (Recuerda, No puedes usar letras)', e)
        n_cuenta = str(n_cuenta)
        return retirar_dinero(n_cuenta, cuentas)


