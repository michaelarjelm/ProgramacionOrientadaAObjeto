# Crea una clase Robot con:
# Atributo privado __temperatura.
# Setter que solo permita modificar la temperatura si está entre 0 y 100 grados.
# Método estado() que muestre:
    # “Normal” si la temperatura está < 70.
    # “Sobrecalentado” si ≥ 70.
# 👉 Prueba asignar valores válidos e inválidos

class Robot:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
    
    def set_temp(self, nueva_temperatura):
        if nueva_temperatura >= 0:
            if nueva_temperatura <= 100:
                self.__temperatura = nueva_temperatura
            else:
                print("La temperatura no puede exceder los 100°C\n")
        else:
            print("La temperatura no puede ser menos que cero\n")


    def estado(self):
        print(f"Temperatura actual: {self.__temperatura}°C")
        if self.__temperatura < 70:
            print("Estado: Normal\n")
        elif self.__temperatura >= 70:
            print("Estado: Sobrecalentado\n")
        

r = Robot(80)
r.estado()
r.set_temp(101)
r.set_temp(-1)
r.set_temp(15)
r.estado()