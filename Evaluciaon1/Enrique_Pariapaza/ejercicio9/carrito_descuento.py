# Representa un producto con su nombre y precio.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Gestiona los productos y cálculos de un carrito de compras.
class Carrito:
    def __init__(self):
        self.productos = {} # Almacena productos y cantidades en un diccionario.

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]['cantidad'] += cantidad
        else:
            self.productos[producto.nombre] = {'producto': producto, 'cantidad': cantidad}
        print(f"{cantidad} unidades de '{producto.nombre}' añadidas al carrito.")

    def calcular_total(self):
        total = 0
        for item in self.productos.values():
            total += item['producto'].precio * item['cantidad']
        return total

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        total_con_descuento = total - descuento
        return total_con_descuento