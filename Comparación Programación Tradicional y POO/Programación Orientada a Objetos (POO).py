# Ejemplo del promedio semanal del clima con Programación Orientada a Objetos (POO)
# Clase que representa la información diaria del clima
class Clima:
    def __init__(self):
        self.temperaturas = []  # Atributo que almacenará las temperaturas diarias

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):  # Suponemos que tenemos 7 días a la semana
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

# Función principal para ejecutar el programa
def main():
    print("Cálculo del promedio semanal de temperaturas.")
    clima = Clima()  # Crear un objeto de la clase Clima
    clima.ingresar_temperaturas()  # Ingresar las temperaturas
    promedio = clima.calcular_promedio()  # Calcular el promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Llamada a la función principal
if __name__ == "__main__":
    main()