from csv import writer, reader

# Función para registrar un movimiento en un archivo CSV
def registrar_movimiento_csv(n_cuenta, tipo_movimiento, monto, saldo_actual):
    #Parámetros:
    #n_cuenta (int): Número de la cuenta.
    #tipo_movimiento (str): 'Retiro' o 'Consignación'.
    #monto (float): Monto del movimiento.
    #saldo_actual (float): Saldo después del movimiento.

    archivo = (f"movimientos_cuenta_{n_cuenta}.csv")

    with open(archivo) as file:
        escritor = writer(file)
        if file.tell() == 0:  # Si el archivo está vacío
            escritor.writerow(["Tipo de Movimiento", "Monto", "Saldo Actual"])  # Encabezados
        escritor.writerow([tipo_movimiento, monto, saldo_actual])  # Escribimos los datos del movimiento

# Función para mostrar movimientos desde un archivo CSV
def mostrar_movimientos_csv(n_cuenta):
    #Muestra los movimientos registrados en un archivo CSV.

    #Parámetros:
    #n_cuenta (int): Número de la cuenta.
    archivo = (f"movimientos_cuenta_{n_cuenta}.csv")