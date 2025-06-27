mostrar_asientos()
    try:
        asiento = int(input("Ingrese el número de asiento que desea comprar: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    if asiento in asientos_disponibles:
        pasajes_vendidos[rut] = asiento
        asientos_disponibles.remove(asiento)
        print(f"Pasaje vendido exitosamente. Asiento {asiento} asignado a RUT {rut}.")
    else:
        print("Asiento no disponible o inválido.")