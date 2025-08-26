class Tienda:
    def __init__(self, nombre, productos=None):
        self.nombre = nombre
        self.productos = productos if productos is not None else []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(p.total() for p in self.productos)

    def mostrar_ticket(self):
        print(f"=== {self.nombre} ===")
        for p in self.productos:
            print(f"{p.nombre} x{p.cantidad} - ${p.precio} c/u  => ${p.total()}")
        print(f"TOTAL: ${self.calcular_total()}")
