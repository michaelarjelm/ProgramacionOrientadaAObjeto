class Item:
    def __init__(self, nombre: str, peso: float):
        self.__nombre = nombre
        self.__peso = peso
        
        
    @property
    def GetNombre(self):
        return self.__nombre
    
    
    @GetNombre.setter
    def SetNombre(self, NuevoNombre):
        if not NuevoNombre:
            print("El valor ingresado no puede estar vacío")
        else:
            self.__nombre = NuevoNombre    
    
    
    @property
    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        if peso <= 0:
            print(" El peso indicado debe ser mayor a cero")
    
    def descripcion_base(self):
        return f"{self.__nombre} (peso: {self.__peso})"
    
    