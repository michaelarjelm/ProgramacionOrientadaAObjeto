# Herencia multiple

'''class Volador:
    def volar(self):
        print("volar")

class Nadador:
    def nadar(self):
        print("nadar")
        
class Pato(Volador,Nadador):
    pass

p= Pato()
p.volar()
p.nadar()'''

# --------------------------------------
# Ejercicio 1

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
            print("El peso no puede ser 0")
        else:
            self.__peso = NuevoPeso
    
    def descripcion_base(self):
        return f"{self.__nombre} (Peso: {self.__peso})"
    

class Pocion(Item):
    def __init__(self, nombre, peso, efecto):
        super().__init__(nombre, peso)
        self.__efecto = efecto
    
    def detalle_pocion(self):
        pass
        