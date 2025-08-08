class Producto:
    def __init__(self):
        # Pedimos valores al usuario
        
        self.nombre = input("Ingresa el nombre del producto: ")
        self.precio = float(input("Ingresa el precio del producto: "))
        self.cantidad = int(input("Ingresa la cantidad en stock: "))

    def mostrar_info(self):
        print("\n📦 Información del producto:")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad: {self.cantidad} unidades")
        print(f"Valor total en inventario: ${self.precio * self.cantidad:.2f}")

# Crear objeto pidiendo datos al usuario
producto1 = Producto()

# Mostrar la información
producto1.mostrar_info()
