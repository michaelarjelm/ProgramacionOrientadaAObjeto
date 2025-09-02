import math


class Circulo:
    def __init__(self, radio):
        self.radio=radio
        
    def calcularArea(self):
        return math.pi * (math.pow(self.radio,2))