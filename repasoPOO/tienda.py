class Tienda:
    def __init__(self):
        self.productos=[]
        
    def agregar_producto(self,producto):
        self.productos.append(producto)
        
    def calcular_total(self):
        totalPrecio=0
        for producto in self.productos:
            totalPrecio+=producto.precio*producto.cantidad
        return totalPrecio