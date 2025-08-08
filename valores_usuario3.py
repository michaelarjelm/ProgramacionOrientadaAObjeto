class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Valor total: ${self.precio * self.cantidad:.2f}")

# Lista para almacenar productos
inventario = []

# Función para agregar productos
def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    inventario.append(Producto(nombre, precio, cantidad))
    print("✅ Producto agregado al inventario.")

# Función para mostrar todos los productos
def mostrar_inventario():
    print("\n📦 Inventario actual:")
    for p in inventario:
        p.mostrar_info()
        print("-" * 20)

# Ejemplo de uso
while True:
    opcion = input("\n1. Agregar producto\n2. Ver inventario\n3. Salir\nElige: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        break
    else:
        print("❌ Opción no válida.")
