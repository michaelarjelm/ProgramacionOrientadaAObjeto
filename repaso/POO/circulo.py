import math
from re import match


class circulo:
    def __init__(self,radio):
        self.radio=radio
        
    def area(self):
        return match.pi  *(math.pow(self.radio,2))