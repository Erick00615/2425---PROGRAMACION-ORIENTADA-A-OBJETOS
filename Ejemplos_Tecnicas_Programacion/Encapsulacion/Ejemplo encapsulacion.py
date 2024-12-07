# Ejemplo de Encapsulación: Gestión de cuenta bancaria con atributos privados

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    def mostrar_saldo(self):
        print(f"Titular: {self.__titular}, Saldo actual: {self.__saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad inválida para depósito.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

# Ejemplo de uso
cuenta = CuentaBancaria("Erick Sarchi", 1000)
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(400)