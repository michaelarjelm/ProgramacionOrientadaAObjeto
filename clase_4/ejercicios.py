class Persona:
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
            print("X Nombre invalido")
            
