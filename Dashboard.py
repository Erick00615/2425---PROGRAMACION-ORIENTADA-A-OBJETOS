import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Aplicación Conceptos de POO en Python/aplicacion_poo.py',
        '2': 'Comparación Programación Tradicional y POO/Programación Orientada a Objetos (POO).py',
        '3': 'Comparación Programación Tradicional y POO/Programación Tradicional.py',
        '4': 'Ejemplos_Tecnicas_Programacion/Abstraccion/Ejemplo abstraccion.py',
        '5': 'Ejemplos_Tecnicas_Programacion/Encapsulacion/Ejemplo encapsulacion.py',
        '6': 'Ejemplos_Tecnicas_Programacion/Herencia/Ejemplo herencia.py',
        '7': 'Ejemplos_Tecnicas_Programacion/Polimorfismo/Ejemplo polimorfismo.py',
        '8': 'EjemplosMundoReal_POO/Tienda.py',
        '9': 'Implementacion de Constructores y Destructores/Constructores_Destructor.py',
        '10': 'Tipos_de_datos_identificadores/Conversion_unidades.py',
    }

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
