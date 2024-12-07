# Ejemplo de Herencia: Clases derivadas de una clase base de vehículos

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def detalles(self):
        super().detalles()
        print(f"Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def detalles(self):
        super().detalles()
        print(f"Cilindrada: {self.cilindrada}cc")

# Ejemplo de uso
auto = Auto("Toyota", "Corolla", 4)
moto = Moto("Yamaha", "R3", 300)

auto.detalles()
moto.detalles()