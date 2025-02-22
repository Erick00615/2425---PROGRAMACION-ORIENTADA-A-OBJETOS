from Inventario import Inventario

def main():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Mostrar Inventario")
        print("2. Agregar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()