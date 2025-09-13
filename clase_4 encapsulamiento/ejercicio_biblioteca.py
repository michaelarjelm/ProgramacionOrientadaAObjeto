# Crea una clase Libro con:
    # Atributo privado __stock.
    # Método prestar() que reduzca el stock en 1 (si hay disponibles).
    # Método devolver() que aumente el stock en 1.
    # Getter stock con @property.
    # 👉 Simula prestar y devolver libros

class Libro:
    def __init__(self, nombre, autor, stock):
        self.nombre = nombre
        self.autor = autor
        self.__stock = stock

    def prestar(self):
        if self.__stock:
            self.__stock -= 1
            print("Prestamo realizado")
        else:
            print(f"Sin stock")
    
    def devolver(self):
        self.__stock += 1
        print("Devolucion realizada")
    
    @property
    def get_stock(self):
        print(f"'{self.nombre}' por {self.autor} | Stock: {self.__stock}")
    
l = Libro("Interpretar", "Rovin", 1)
l.prestar()
l.get_stock
l.prestar()
l.devolver()
l.get_stock
    
