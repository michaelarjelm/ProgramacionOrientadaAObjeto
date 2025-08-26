class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def presentarse (self):
        print("Hola, me llamo ",self.nombre," y tengo ",self.edad," años." )