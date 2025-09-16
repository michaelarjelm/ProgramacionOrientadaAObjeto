# Ejercicio repaso

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcularTotal(self):
        return self.precio * self.cantidad
    
class Tienda:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto) # composicion
        
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio * producto.cantidad
        return total
    
    
a = Producto("dd",200,5)
b= Producto("cc",300,2)
c=  Producto("gg",500,3)   
t = Tienda()
t.agregar_producto(a)
t.agregar_producto(b)
t.agregar_producto(c)
print(t.calcular_total())