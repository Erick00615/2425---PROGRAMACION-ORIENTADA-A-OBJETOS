# Objetivo: Desarrollar un sistema de gestión de inventarios simple para una tienda, que permita añadir, actualizar, eliminar y buscar productos utilizando una estructura de datos personalizada.

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        """Inicializa el inventario como una lista vacía"""
        self.productos = []

    def agregar_producto(self, producto):
        """Añade un producto al inventario asegurando que el ID sea único"""
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: ID de producto duplicado.")
            return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID"""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto por su ID"""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre"""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else "No se encontraron productos."

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


# Interfaz de Usuario en la Consola
def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for prod in resultados:
                    print(prod)
            else:
                print(resultados)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar menú interactivo
if __name__ == "__main__":
    menu()
