if opcion == "1":
            mostrar_asientos()
        elif opcion == "2":
            vender_pasaje()
        elif opcion == "3":
            print("\nPasajes vendidos:")
            for rut, asiento in pasajes_vendidos.items():
                print(f"RUT: {rut} - Asiento: {asiento}")
        elif opcion == "4":
            print("Gracias por usar PasajeBus. ¡Buen viaje!")
            break
        else:
            print("Opción no válida.")

menu()
