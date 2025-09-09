class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustible = 100   # empieza con tanque lleno

    def conducir(self, km):
        if km <= self.combustible:
            self.combustible = self.combustible - km
            print(f"Condujiste {km} km. Combustible restante: {self.combustible}.")
        else:
            print("No tienes suficiente combustible para recorrer esa distancia.")

    def recargar(self, cantidad):
        self.combustible = self.combustible+cantidad
        print(f"Recargaste {cantidad}. Combustible actual: {self.combustible}.")
