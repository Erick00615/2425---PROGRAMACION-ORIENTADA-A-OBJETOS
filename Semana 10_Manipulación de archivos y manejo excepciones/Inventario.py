# Objetivo: Mejorar el sistema de gestión de inventarios desarrollado anteriormente para que utilice archivos para
# almacenar y recuperar la información del inventario y maneje excepciones durante la lectura y escritura de archivos.
import os


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de texto."""
        if not os.path.exists(self.archivo):
            return []
        productos = []
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    productos.append({"nombre": datos[0], "cantidad": int(datos[1]), "precio": float(datos[2])})
        except FileNotFoundError:
            print("Error: El archivo de inventario no fue encontrado.")
        except PermissionError:
            print("Error: No se tiene permiso para leer el archivo.")
        return productos

    def guardar_inventario(self):
        """Guarda los productos en el archivo de texto."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto['nombre']},{producto['cantidad']},{producto['precio']}\n")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario y lo guarda en el archivo."""
        self.productos.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, nombre, nueva_cantidad, nuevo_precio):
        """Actualiza un producto en el inventario y lo guarda en el archivo."""
        for producto in self.productos:
            if producto["nombre"] == nombre:
                producto["cantidad"] = nueva_cantidad
                producto["precio"] = nuevo_precio
                self.guardar_inventario()
                print(f"Producto '{nombre}' actualizado exitosamente.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario y lo guarda en el archivo."""
        for producto in self.productos:
            if producto["nombre"] == nombre:
                self.productos.remove(producto)
                self.guardar_inventario()
                print(f"Producto '{nombre}' eliminado exitosamente.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(
                    f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}")