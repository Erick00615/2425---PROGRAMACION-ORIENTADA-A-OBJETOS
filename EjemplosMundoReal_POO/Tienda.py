# Objetivo: Aplicar y demostrar la comprensión de los conceptos de Programación Orientada a Objetos (POO) mediante la creación de ejemplos que modelen situaciones del mundo real.
# Ejemplo Tienda

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f'{self.nombre} ({self.categoria}) - ${self.precio}'

# Clase Carrito
class Carrito:
    def __init__(self):
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for producto in self.productos:
                print(producto)
            print(f'Total: ${self.total:.2f}')

    def aplicar_descuento(self, porcentaje_descuento):
        descuento = self.total * (porcentaje_descuento / 100)
        total_con_descuento = self.total - descuento  # Calculamos el total con descuento
        return descuento, total_con_descuento  # Retornamos el descuento y el total con descuento

# Crear productos
producto1 = Producto("Laptop", 1200, "Electrónica")
producto2 = Producto("Camiseta", 25, "Ropa")
producto3 = Producto("Auriculares", 150, "Electrónica")

# Crear un carrito y agregar productos
carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

# Mostrar carrito antes del descuento
print("Carrito de compras antes del descuento:")
carrito.mostrar_carrito()

# Aplicar descuento del 10%
descuento, total_con_descuento = carrito.aplicar_descuento(10)

# Mostrar el descuento aplicado y el total con descuento
print(f"\nDescuento aplicado: ${descuento:.2f}")
print(f"Total con descuento: ${total_con_descuento:.2f}")