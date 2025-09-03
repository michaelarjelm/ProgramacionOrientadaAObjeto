# Esta clase representa un artículo en un pedido.
class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def subtotal(self):
        return self.precio * self.cantidad
        
# Esta clase gestiona un pedido que contiene varios artículos.
class Pedido:
    def __init__(self):
        self.items = []
        
    def agregar_item(self, item):
        self.items.append(item)
        print(f"Se ha agregado '{item.nombre}' al pedido.")
        
    def calcular_total(self):
        total = sum(item.subtotal() for item in self.items)
        return total