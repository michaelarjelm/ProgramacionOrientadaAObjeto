from tienda import Tienda
from producto import Producto

tienda=Tienda()

productoUno=Producto("monitor", 100000, 2)
productoDos=Producto("teclado", 200000, 3)

tienda.agregar_producto(productoUno)
tienda.agregar_producto(productoDos)

total=tienda.calcular_total()

print(f"El total de su compra es {total}")
