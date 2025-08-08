class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        
    
        
nombre=input("Ingresa el nombre del producto: ")
precio=float(input("Ingresa el precio del producto: "))
cantidad=int(input("Ingresa el stock del producto: "))
    
productoPrueba = Producto(nombre,precio, cantidad)

def mostrar_info(producto):
        print("\n📦 Información del producto:")
        print(f"Nombre: {producto.nombre}")
        print(f"Precio: ${producto.precio:.2f}")
        print(f"Cantidad: {producto.stock} unidades")
        print(f"Valor total en inventario: ${producto.precio * producto.stock:.2f}")

mostrar_info(productoPrueba)
