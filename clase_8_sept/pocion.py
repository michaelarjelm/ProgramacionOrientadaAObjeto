from clase_8_sept.item import Item

class Pocion(Item):
    def __init__(self, nombre, peso, efecto):
        super().__init__(nombre, peso)
        self.__efecto = efecto
        
        
p = Pocion("Pocion de cura", 1.5, "curar PV")
print(p.getPeso)