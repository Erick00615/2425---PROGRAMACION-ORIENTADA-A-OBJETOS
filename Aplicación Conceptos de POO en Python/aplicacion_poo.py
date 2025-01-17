#Objetivo:
#Aplicar los conocimientos adquiridos sobre Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo en Python para desarrollar un programa.

# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."


# Clase derivada: Empleado (herencia de Persona)
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto, salario):
        super().__init__(nombre, edad)
        self.__puesto = puesto  # Atributo encapsulado
        self.salario = salario

    # Metodo para acceder al atributo encapsulado
    def obtener_puesto(self):
        return self.__puesto

    # Metodo sobrescrito para demostrar polimorfismo
    def saludar(self):
        return f"Hola, soy {self.nombre} y trabajo como {self.__puesto}."

    # Metodo adicional para calcular un bono basado en el salario
    def calcular_bono(self, porcentaje):
        return self.salario * porcentaje / 100


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Persona
    persona = Persona("Erick", 30)
    print(persona.mostrar_informacion())
    print(persona.saludar())

    # Crear una instancia de Empleado
    empleado = Empleado("Ana", 28, "Ingeniera de Software", 2500)
    print(empleado.mostrar_informacion())
    print(empleado.saludar())
    print(f"Puesto: {empleado.obtener_puesto()}")
    print(f"Bono (10%): {empleado.calcular_bono(10)}")