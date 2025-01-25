# Objetivo de la Tarea:
# Aplicar los conceptos aprendidos sobre constructores y destructores para desarrollar un programa en Python.

class Vehiculo:
    # Constructor: inicializa los atributos del objeto
    def __init__(self, marca, modelo, año):
        """
        Este es el constructor de la clase Vehiculo.
        Se llama cuando se crea una nueva instancia de la clase.

        Inicializa los atributos del objeto: marca, modelo, y año.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"Vehículo {self.marca} {self.modelo} del año {self.año} ha sido creado.")

    # Destructor: se llama cuando el objeto es destruido o eliminado
    def __del__(self):
        """
        Este es el destructor de la clase Vehiculo.
        Se llama cuando el objeto es destruido o cuando ya no tiene referencias activas.

        Aquí se puede liberar cualquier recurso si fuera necesario.
        """
        print(f"Vehículo {self.marca} {self.modelo} ha sido destruido.")


# Crear una instancia de la clase Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla", 2020)

# Eliminar la instancia del objeto, lo que desencadenará la llamada al destructor
del mi_vehiculo

# Crear una segunda instancia de la clase Vehiculo
otro_vehiculo = Vehiculo("Honda", "Civic", 2022)

# El objeto 'otro_vehiculo' se eliminará automáticamente cuando el programa termine,
# lo que causará que se ejecute el destructor al finalizar el ciclo de vida del objeto.