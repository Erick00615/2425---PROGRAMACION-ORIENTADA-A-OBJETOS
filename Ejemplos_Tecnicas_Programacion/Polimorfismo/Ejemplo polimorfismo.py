# Ejemplo de Polimorfismo: Métodos que se comportan de manera diferente según la clase

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "El perro ladra: ¡Guau, guau!"

class Gato(Animal):
    def sonido(self):
        return "El gato maúlla: ¡Miau, miau!"

class Vaca(Animal):
    def sonido(self):
        return "La vaca muge: ¡Muuu!"

def imprimir_sonido(animal):
    print(animal.sonido())

# Ejemplo de uso
perro = Perro()
gato = Gato()
vaca = Vaca()

imprimir_sonido(perro)
imprimir_sonido(gato)
imprimir_sonido(vaca)
