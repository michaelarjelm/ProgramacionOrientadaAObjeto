# Crea una clase Jugador con:
# Atributo privado __vida (máximo 100).
# Método recibir_dano(cantidad) que reste vida (sin bajar de 0).
# Método curar(cantidad) que aumente vida (sin superar 100).
# Getter vida con @property.
# 👉 Simula que un jugador recibe daño y luego se cura.

class Jugador:
    def __init__(self):
        self.__vida = 100

    def recibir_daño(self, daño):
        if self.__vida == 0:
            return f"Stop! he's already dead"
        elif self.__vida - daño > 0:
            self.__vida -= daño
            return f"Recibiste {daño} puntos de daño."
        else:
            self.__vida = 0
            return f"Recibiste {daño} puntos de daño. Te quedaste sin vida"
 
    def curar(self, cura):
        if self.__vida == 100:
            return "Ya estas full de vida"
        elif self.__vida + cura <= 100:
            self.__vida += cura
            return f"Recibiste {cura} puntos de cura."
        else:
            self.__vida = 100
            return "Recibiste mas cura de lo que necesitabas, ahora estas a full"

    @property
    def vida(self):
        return f"Tu vida actual es de {self.__vida} puntos"

player1 = Jugador()
print(player1.vida)
print(player1.curar(13))
print(player1.recibir_daño(40))
print(player1.recibir_daño(30))
print(player1.recibir_daño(70))
print(player1.vida)
print(player1.curar(30))
print(player1.recibir_daño(35))
print(player1.recibir_daño(40))
print(player1.vida)
print(player1.curar(200))