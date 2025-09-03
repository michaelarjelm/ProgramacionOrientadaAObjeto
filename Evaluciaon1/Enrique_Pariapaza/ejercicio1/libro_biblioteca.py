# Crea la clase Libro con sus atributos (título, autor, copias).
class Libro:
    def __init__(self, titulo, autor, copias):
        # Asigna los valores iniciales a las propiedades del libro.
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
        
# Crea la clase Biblioteca, que contiene y gestiona los libros.
class Biblioteca:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los libros.
        self.libros = []
        
    def agregar_libro(self, libro):
        # Añade un libro a la lista de la biblioteca.
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")
        
    def prestar_libro(self, titulo):
        # Busca el libro por su título y reduce el número de copias disponibles.
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.copias > 0:
                    libro.copias -= 1
                    print(f"Has prestado una copia de '{libro.titulo}'. Quedan {libro.copias} copias.")
                    return
                else:
                    print(f"No hay copias disponibles de '{titulo}'.")
                    return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
        
    def devolver_libro(self, titulo):
        # Busca el libro y aumenta el número de copias disponibles.
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
                print(f"Has devuelto una copia de '{libro.titulo}'. Hay {libro.copias} copias ahora.")
                return
        print(f"No se puede devolver '{titulo}' porque no se encuentra en la biblioteca.")
        
    def mostrar_libros(self):
        # Muestra los detalles de cada libro.
        if not self.libros:
            print("La biblioteca está vacía.")
            return
        
        print("\n--- Listado de Libros en la Biblioteca ---")
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Copias: {libro.copias}")
            