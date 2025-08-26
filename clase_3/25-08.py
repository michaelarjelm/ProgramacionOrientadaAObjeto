# (?) jerarquia de clases
# una clase es una plantilla o modelo

# ejemplo:

'''class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mostrar_info(self):
        print("Coche:", self.marca, self.modelo)
        
auto1 = Coche("Toyta", "Corlla")
auto1.mostrar_info()'''

# ------------------estructura-----------(quizas)---

# class NombreClase:
#     def __init__(self, parametro):
#         self.parametro = parametro

#     def metodo(self):
#         print(self.parametro)

# --------------------------------------------------
        
# ejercicio:

# Crea una clase llamada Circulo que tenga:
# Un constructor que reciba el radio como parámetro.
# Un método llamado área que calcule y devuelva el área
# del círculo (usa la fórmula: área = π * radio^2).

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * (math.pow(self.radio, 2))

# Instrucciones:
# Crea una instancia de Circulo con radio 5.
# Llama al método área e imprime el resultado.

circulo = Circulo(5)
area = circulo.area()
print("El area es:", area)

from clase_Persona import Persona

persona1 = Persona("Rovin", 27)
persona2 = Persona("Foster", 30)

persona1.presentarse()
persona2.presentarse()