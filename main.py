import datetime

def elegir_fecha():
    # Lista de fechas a elegir y sus nombres correspondientes
    fechas_posibles = [
        ("10/10", "Manurro"),  # Fecha y nombre
        ("21/09", "Matute"),   # Respuesta correcta
        ("22/11", "Marga"),
        ("25/04", "Apa")
    ]
    
    # Muestra las fechas posibles al usuario
    print("Elige una de las siguientes fechas:")
    for i, (fecha, nombre) in enumerate(fechas_posibles, start=1):
        print(f"{i}. {fecha} ({nombre})")
    
    # Pide la opción del usuario
    try:
        opcion = int(input("Elige el número de la fecha correcta (1-4): "))
        if opcion < 1 or opcion > 4:
            print("Opción inválida. Elige un número entre 1 y 4.")
            return False
    except ValueError:
        print("Por favor, introduce un número válido entre 1 y 4.")
        return False

    # La fecha correcta y su nombre
    fecha_correcta = "21/09"  # Fecha correcta
    nombre_correcto = "Matute"  # Nombre correcto

    # Compara la opción elegida con la fecha correcta
    fecha_elegida, nombre_elegido = fechas_posibles[opcion - 1]
    
    if fecha_elegida == fecha_correcta:
        print(f"¡Correcto! El regalo viene de {nombre_elegido}.")
        return True
    else:
        print(f"¡Incorrecto! Sigue buscando... La fecha {fecha_elegida} corresponde a {nombre_elegido}.")
        return False

# Llamamos a la función para ejecutar el código
elegir_fecha()
