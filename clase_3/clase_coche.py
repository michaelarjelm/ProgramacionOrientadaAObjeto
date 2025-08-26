# ejercicio 3

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustible = 100
        
    def conducir(self, km):
        if km <= self.combustible:
            self.combustible = self.combustible - km
            print(f"Condujiste {km}. Combustible restante: {self.combustible}")
        else:
            print("No tienes suficiente combustible")
            
    def recarga(self, cantidad):
        self.combustible += cantidad
        print(f"Recargaste: {cantidad} lts. Combustible actual: {self.combustible}")
        
        
coche = Coche("Ford", "Corssel")
coche.conducir(5)
coche.recarga(20)