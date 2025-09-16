class Producto:
    def __init__(self ,nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        
    def calcularTotal(self):
        return self.precio*self.cantidad
      
        