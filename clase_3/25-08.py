# (?) jerarquia de clases
# una clase es una plantilla o modelo

# ejemplo:
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mostrar_info(self):
        print("Coche:", self.marca, self.modelo)
        
auto1 = Coche("Toyta", "Corlla")
auto1.mostrar_info()
        
# ejercicio:


        