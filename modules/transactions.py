# 4. Función: Retirar Dinero
def retirar_dinero(n_cuenta, monto, cuentas):
    #Parámetros:
    #id_cuenta (int): Número de la cuenta desde la que se quiere retirar.
    #monto (float): Monto de dinero a retirar.
    #cuentas (dict): Diccionario con las cuentas y sus datos.

    #Verificar si la cuenta existe en el diccionario de cuentas
    if n_cuenta in cuentas:
        password = int(input("Ingrese su clave: "))
        if password == cuentas[n_cuenta]:
            saldo = cuentas[n_cuenta]
            # Verificar si hay suficiente saldo para realizar el retiro
            if monto > 0 and monto <= saldo:
                cuentas[n_cuenta] -= monto  # Restar el monto del saldo
                print(f"Se retiraron ${monto}")
                print(f"Saldo actual: ${cuentas[n_cuenta]}")
            elif monto > saldo:
                print("Error: Fondos insuficientes.")
            else:
                print("Error: El monto debe ser mayor que 0.")
        else:
            print("Error: Clave incorrecta.")
    else:
        print("Error: La cuenta no existe.")



def pagar_servicios2(id_cuenta, monto, servicio):
    if id_cuenta in cuentas: # Verificacion de que la cuenta existe
        if monto > 0: 
            print(f"Se consignó {monto} en la cuenta {id_cuenta}")
            print(f"Su saldo actual es: {saldo}")
        else:
            print("Dinero insuficiente para pagar el servicio")
    else:
        print("La cuenta no existe")