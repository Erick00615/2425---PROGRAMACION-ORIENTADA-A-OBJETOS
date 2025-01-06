# Programa para convertir unidades de longitud (metros a otras unidades)
# Este programa convierte un valor ingresado en metros a kilómetros, centímetros y milímetros.

def convertir_unidades(longitud_en_metros):
    """
    Función para convertir una longitud en metros a otras unidades de medida:
    kilómetros, centímetros y milímetros.

    Parámetros:
    longitud en metros (float): El valor en metros a convertir.

    Retorna:
    dict: Un diccionario con las conversiones a kilómetros, centímetros y milímetros.
    """
    # Conversiones
    longitud_en_km = longitud_en_metros / 1000  # 1 km = 1000 metros
    longitud_en_cm = longitud_en_metros * 100  # 1 metro = 100 centímetros
    longitud_en_mm = longitud_en_metros * 1000  # 1 metro = 1000 milímetros

    # Almacenar resultados en un diccionario
    conversiones = {
        "kilómetros": longitud_en_km,
        "centímetros": longitud_en_cm,
        "milímetros": longitud_en_mm
    }

    return conversiones


# Solicitar al usuario que ingrese un valor en metros
longitud_en_metros = float(input("Ingresa la longitud en metros: "))

# Convertir la longitud a otras unidades
conversiones = convertir_unidades(longitud_en_metros)

# Mostrar los resultados
print(f"\nConversión de {longitud_en_metros} metros:")
for unidad, valor in conversiones.items():
    print(f"{valor:.2f} {unidad}")