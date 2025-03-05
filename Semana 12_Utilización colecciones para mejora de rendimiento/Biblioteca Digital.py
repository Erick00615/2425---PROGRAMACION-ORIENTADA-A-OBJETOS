#Objetivo: Desarrollar un sistema para gestionar una biblioteca digital. El sistema permitirá administrar los libros
#disponibles, las categorías de libros, los usuarios registrados y el historial de préstamos.

# Clase Libro: Representa un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Atributos inmutables: título y autor como tuplas
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} de {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario: Representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca: Gestiona los libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros (ISBN como clave y objeto Libro como valor)
        self.usuarios = set()  # Conjunto de IDs de usuarios registrados

    # Método para añadir un libro
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    # Método para quitar un libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    # Método para registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Método para dar de baja a un usuario
    def dar_baja_usuario(self, id_usuario):
        usuario_a_borrar = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario_a_borrar:
            self.usuarios.remove(usuario_a_borrar)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    # Método para prestar un libro a un usuario
    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} ya tiene el libro '{libro.titulo}' prestado.")
        else:
            print("Libro o usuario no encontrado.")

    # Método para devolver un libro
    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene el libro '{libro.titulo}' prestado.")
        else:
            print("Libro o usuario no encontrado.")

    # Método para buscar un libro por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.libros.values() if getattr(libro, criterio, "").lower() == valor.lower()]

        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    # Método para listar los libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")


# Crear la biblioteca y objetos
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "978-3-16-148411-7")

# Crear algunos usuarios
usuario1 = Usuario("Erick Sarchi", "U001")
usuario2 = Usuario("Ana Pérez", "U002")

# Añadir libros y registrar usuarios
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros a usuarios
biblioteca.prestar_libro("978-3-16-148410-0", "U001")
biblioteca.prestar_libro("978-3-16-148411-7", "U002")

# Listar libros prestados por un usuario
biblioteca.listar_libros_prestados("U001")

# Buscar libros por autor
biblioteca.buscar_libro("autor", "Gabriel García Márquez")

# Devolver libros
biblioteca.devolver_libro("978-3-16-148410-0", "U001")

# Listar libros prestados después de devolver uno
biblioteca.listar_libros_prestados("U001")

# Quitar un libro de la biblioteca
biblioteca.quitar_libro("978-3-16-148411-7")