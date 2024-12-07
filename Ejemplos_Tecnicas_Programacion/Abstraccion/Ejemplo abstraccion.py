# Ejemplo de Abstracción: Implementación de clases abstractas para definir roles de personajes

from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    @abstractmethod
    def atributos(self):
        pass

    @abstractmethod
    def atacar(self, enemigo):
        pass

class Guerrero(Personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atributos(self):
        print(f"Guerrero: {self.nombre}")
        print(f"Vida: {self.vida}, Fuerza: {self.fuerza}")

    def atacar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        enemigo.vida -= max(daño, 0)
        print(f"{self.nombre} ataca a {enemigo.nombre}, causando {max(daño, 0)} de daño.")

class Arquero(Personaje):
    def __init__(self, nombre, vida, precision):
        super().__init__(nombre, vida)
        self.precision = precision

    def atributos(self):
        print(f"Arquero: {self.nombre}")
        print(f"Vida: {self.vida}, Precisión: {self.precision}")

    def atacar(self, enemigo):
        daño = self.precision * 2 - enemigo.defensa
        enemigo.vida -= max(daño, 0)
        print(f"{self.nombre} dispara a {enemigo.nombre}, causando {max(daño, 0)} de daño.")

# Ejemplo de uso
guerrero = Guerrero("Erick el Valiente", 120, 35)
arquero = Arquero("Sarchi el Silencioso", 90, 40)

guerrero.atributos()
arquero.atributos()