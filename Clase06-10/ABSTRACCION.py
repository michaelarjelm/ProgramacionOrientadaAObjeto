#Qué es la abstracción: cumplen la función de tipo "contrato", qué es un contrato--> Hace relación a una interfaz.
#No se pueden instanciar. Se puede edefinir como una plantilla de clases 
#para utilizarlo es necesario importar ABC: from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
class Mensaje(ABC):
    def 