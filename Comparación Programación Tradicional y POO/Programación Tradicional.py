# Ejemplo del promedio semanal del clima con Programación Tradicional
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Suponemos que tenemos 7 días a la semana
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal para ejecutar el programa
def main():
    print("Cálculo del promedio semanal de temperaturas.")
    temperaturas = ingresar_temperaturas()  # Ingresamos las temperaturas
    promedio = calcular_promedio(temperaturas)  # Calculamos el promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Llamada a la función principal
if __name__ == "__main__":
    main()