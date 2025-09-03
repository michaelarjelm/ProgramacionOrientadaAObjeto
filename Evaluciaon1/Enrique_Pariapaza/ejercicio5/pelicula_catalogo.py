# Esta clase modela una película con sus características principales.
class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        
# Esta clase representa un catálogo que organiza y gestiona películas.
class Catalogo:
    def __init__(self):
        self.peliculas = []
        
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"La película '{pelicula.titulo}' ha sido agregada al catálogo.")
        
    def filtrar_por_genero(self, genero):
        return [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        
    def buscar_por_titulo(self, titulo):
        for p in self.peliculas:
            if p.titulo.lower() == titulo.lower():
                return p
        return None
        
    def listar_todas(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
            return
        
        print("\n--- Listado de Películas ---")
        for p in self.peliculas:
            print(f"Título: {p.titulo}, Género: {p.genero}, Año: {p.anio}")