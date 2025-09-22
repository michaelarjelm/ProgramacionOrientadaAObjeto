# Parte 1 – Clase base Item
# Define una clase Item que represente un objeto genérico.
# Debe tener dos atributos privados:
    # __nombre → el nombre del ítem.
    # __peso → el peso del ítem.
# Usa encapsulamiento con @property y @setter para que:
    # El nombre no pueda estar vacío.
    # El peso siempre sea mayor que 0.
# Implementa un método descripcion_base() que devuelva un texto como: “"Poción de curación (peso: 0.5)"

class Item:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso
    
    @property
    def GetNombre(self):
        return self.__nombre    

    @GetNombre.setter
    def SetNombre(self, NuevoNombre):
        # if len(self.__nombre) == 0:  # Otra forma
        if not NuevoNombre:
            print("El nombre no puede estar vacio")
        self.__nombre = NuevoNombre # Se puede usar else, pero tambien se puede hacer asi
        
    @property
    def GetPeso(self):
        return self.__peso
    
    @GetPeso.setter
    def SetPeso(self, NuevoPeso):
        if NuevoPeso <= 0:
            print("El peso no puede ser menor o igual a cero")
        else:
            self.__peso = NuevoPeso
    
    def descripcion_base(self):
        return f"{self.__nombre} (Peso: {self.__peso})"
    
# -----------------------------------------------------------------------  
# Parte 2 – Subclases específicas
# 1.Poción (Pocion)
# Hereda de Item.
# Agrega un atributo privado __efecto que describe qué hace la poción.
# Define un método detalle_pocion() que:
    # Llame al método descripcion_base() del padre.
    # Añada el efecto de la poción al texto final.

class Pocion(Item):
    def __init__(self, nombre, peso, efecto):
        super().__init__(nombre, peso)
        self.__efecto = efecto
    
    def detalle_pocion(self):
        return f"{super().descripcion_base()} Efecto: {self.__efecto}"
        
# -----------------------------------------------------------------------        
# 2.Arma (Arma)
# Hereda de Item.
# Agrega un atributo privado __daño que indica el daño que causa el arma.
# Define un método detalle_arma() que:
    # Llame al método descripcion_base() del padre.
    # Añada el daño del arma al texto final.

class Arma(Item):
    def __init__(self, nombre, peso, daño):
        super().__init__(nombre, peso)
        self.__daño = daño

    def detalle_arma(self):
        return f"{super().descripcion_base()} Daño: {self.__daño}"
    
# Crea un objeto Pocion llamado "Poción de curación", con peso 0.5 y efecto "Recupera 50 HP".
# Crea un objeto Arma llamado "Espada larga", con peso 3.0 y daño 25.
# Llama a los métodos detalle_pocion() y detalle_arma() para mostrar la información completa de cada objeto.
# Intenta asignar un peso negativo a alguno de los objetos y captura la excepción para mostrar que el encapsulamiento funciona.

pocion = Pocion("Poción de curación", 0.5, "Recupera 50 HP")
arma = Arma("Espada larga", 3.0, 25)

print(pocion.detalle_pocion())
print(arma.detalle_arma())

arma.SetPeso = -12
arma.SetPeso = 0
arma.SetPeso = 0.6
print(arma.descripcion_base())

