class Coche:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.combustible=100
        
    def conducir(self,km):
        if km<=self.combustible:
            self.combustible=self.combustible-km
            print(f"Condujiste {km}. Combustible restante: {self.combustible}")
        else:
            print("No tienes el combustible suficiente para este recorrido")
            
    def recargar(self, cantidad):
        self.combustible=self.combustible+cantidad
        print(f"Recargaste {cantidad} litros. Combustible actual: {self.combustible}")