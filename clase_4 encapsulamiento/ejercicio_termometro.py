# Crea una clase Termometro con:
    # Atributo privado __celsius.
    # Getter y setter con @property.
    # Si alguien intenta asignar una temperatura menor a -273 (cero absoluto), mostrar error.
    # Método fahrenheit() que devuelva la conversión.
    # 👉 Crea un termómetro y muestra la temperatura en ambas escalas.

class Termometro:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    # Getter
    @property
    def farenheit(self):
        conversion = self.__celsius * 1.8 + 32
        return f"{self.__celsius}°C son {conversion:.1f}°F"
    
    # Getter
    @property
    def celsius(self):
        return f"La temperatura actual es de {self.__celsius}°C"

    # Setter
    @celsius.setter
    def celsius(self, nueva_temperatura):
        if nueva_temperatura >= -273:
             self.__celsius = nueva_temperatura
             print(f"Se cambio la temperatura a {self.__celsius}°C")
        else:
            print("La temperatura no puede ser menor a -273°C")

t = Termometro(37)

print(t.farenheit)
print(t.celsius)
t.celsius = 34
t.celsius = -300
t.celsius = 0
print(t.farenheit)