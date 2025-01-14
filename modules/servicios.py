from modules.error_messages import saldo_insuficiente

def pagar_servicio_energia(arreglo, n_cuenta):
    if int(n_cuenta) in arreglo:
        n_cuenta = int(n_cuenta)
        referencia = input('Ingrese el numero de referencia del servicio')
        match referencia:
            case '001':
                print('Pagar Servicio Energia')
                saldo = arreglo[n_cuenta]['BILLETERA']
                if int(saldo) < 85000:
                    saldo_insuficiente()
                    return
                arreglo[n_cuenta]['BILLETERA'] -= 85000
                print('Servicio pagado correctamente')
            case _:
                print('Ups, Recuerda el numero de referencia')
                return
    else:
        print('Lo siento, Cuenta no encontrada')

def pagar_servicio_gas(arreglo, n_cuenta):
    if int(n_cuenta) in arreglo:
        n_cuenta = int(n_cuenta)
        referencia = input('Ingrese el numero de referencia del servicio')
        match referencia:
            case '002':
                print('Pagar Servicio Gas')
                saldo = arreglo[n_cuenta]['BILLETERA']
                if int(saldo) < 15000:
                    saldo_insuficiente()
                    return
                arreglo[n_cuenta]['BILLETERA'] -= 15000
                print('Servicio pagado correctamente')
            case _:
                print('Ups, Recuerda el numero de referencia')
    else:
        print('Lo siento, Cuenta no encontrada')

def pagar_servicio_agua(arreglo, n_cuenta):
    if int(n_cuenta) in arreglo:
        n_cuenta = int(n_cuenta)
        referencia = input('Ingrese el numero de referencia del servicio')
        match referencia:
            case '003':
                print('Pagar Servicio Agua')
                saldo = arreglo[n_cuenta]['BILLETERA']
                if int(saldo) < 100000:
                    saldo_insuficiente()
                    return
                arreglo[n_cuenta]['BILLETERA'] -= 100000
                print('Servicio pagado correctamente')
            case _:
                print('Ups, Recuerda el numero de referencia')
    else:
        print('Lo siento, Cuenta no encontrada')