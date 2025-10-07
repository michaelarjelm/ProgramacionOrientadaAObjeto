from abc import ABC, abstractmethod

class Pago (ABC):
    @abstractmethod
    def procesar (self, monto):
        pass