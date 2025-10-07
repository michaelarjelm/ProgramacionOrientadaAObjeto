from abc import ABC, abstractmethod

# clase abstracta
class Pago(ABC):
    @abstractmethod
    def procesar(self, monto):
        pass
    
