# Parte 1 – Clase base Item
# Define una clase Item que represente un objeto
# genérico.
# Debe tener dos atributos privados:
# __nombre → el nombre del ítem.
# __peso → el peso del ítem.
# Usa encapsulamiento con @property y @setter para
# que:
# El nombre no pueda estar vacío.
# El peso siempre sea mayor que 0.
# Implementa un método descripcion_base() que
# devuelva un texto como: “"Poción de curación (peso:
# 0.5)"

class Item:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nuevo_nombre):
        if not nuevo_nombre:
            print("El nombre no puede estar vacio")
        self.__nombre = nuevo_nombre

    @property
    def peso(sefl):
        return sefl.__peso
    
    @peso.getter
    def peso(self, peso):
        if peso<=0:
            print ("El peso ")