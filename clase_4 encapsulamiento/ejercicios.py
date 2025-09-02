class CocheElectrico:
    def __init__(self, bateria):
        self.__bateria = bateria
        
    def cargar(self, energia):
        if self.__bateria < 100:
            if self.__bateria + energia <= 100:
                self.__bateria += energia
                print(f"Cargaste un {energia}%, tu bateria esta al {self.__bateria}%")
            else:
                print(f"Estas cargando {energia}% pero nivel de carga supera el tope, tienes {self.__bateria}% de bateria")
        else:
            print("Tu bateria esta llena")
            
    
    def conducir(self, km):
        if self.__bateria > 0:
            if self.__bateria - km >= 0:
                self.__bateria -= km
                print(f"Condujiste {km} kms. Te queda {self.__bateria}% bateria")
            else:
                print(f"No tienes suficiente bateria para conducir {km} kms. Te queda {self.__bateria}% bateria")
        else:
            print("No tienes bateria para conducir.")
            
auto = CocheElectrico(100)
auto.conducir(10)
auto.conducir(25)
auto.conducir(120)
auto.cargar(80)
auto.cargar(15)
