def consignar_dinero(id_cuenta, monto, arreglo):
    if id_cuenta in arreglo: # Verificacion de que la cuenta existe
        if monto > 0: 
            print(f"Se consignó {monto} en la cuenta {id_cuenta}")
            print(f"Su saldo actual es: {saldo}")
        else:
            print("Dinero insuficiente")
    else:
        print("La cuenta no existe")

def retirar_dinero(id_cuenta, monto):
    if id_cuenta in cuentas: # Verificacion de que la cuenta existe
        if monto > 0: 
            print(f"Se retiró {monto} en la cuenta {id_cuenta}")
            print(f"Su saldo actual es: {saldo}")
        else:
            print("Dinero insuficiente")
    else:
        print("La cuenta no existe")

def pagar_servicios2(id_cuenta, monto, servicio):
    if id_cuenta in cuentas: # Verificacion de que la cuenta existe
        if monto > 0: 
            print(f"Se consignó {monto} en la cuenta {id_cuenta}")
            print(f"Su saldo actual es: {saldo}")
        else:
            print("Dinero insuficiente para pagar el servicio")
    else:
        print("La cuenta no existe")