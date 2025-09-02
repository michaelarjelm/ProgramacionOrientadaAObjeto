'''class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre      # Atributo privado
        self.__edad = edad         # Atributo privado
    
    # Getter
    def get_nombre(self):
        return self.__nombre
    
    # Setter
    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("X Nombre invalido")'''
            
# -------------------------------------------------------------------------
'''
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        
persona = Persona("Alondra")
print(persona._nombre)''' # malo, no se deberia hacer porque es un atributo protegido

# -------------------------------------------------------------------------

'''class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre # privado
        
persona = Persona("Alondra")
print(persona.__nombre)''' # da error, porque es un atributo privado y no puede acceder a el

# -------------------------------------------------------------------------

# hay que definir un get:
'''class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre): # no es necesario que siempre se defina un set
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("nombre invalido")
        
persona = Persona("Alondra")
print(persona.get_nombre())
persona.set_nombre("caca")'''

# ------- DECORADORES ------------------------------------------------------------------

class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    
    @property
    def nombreCompleto(self):
        return f"{self.__nombre} {self.__apellido}" 
    
    @nombreCompleto.setter
    def cambiarNombre(self, nuevo_nombre): # no es necesario que siempre se defina un set
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("nombre invalido")
            
persona = Persona("Alondra", "Gonzalez")
print(persona.nombreCompleto)

persona.cambiarNombre="ddddd"
print(persona.nombreCompleto)

