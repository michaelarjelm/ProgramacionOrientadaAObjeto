# Definimos una clase llamada Persona
class Persona:
    # El método __init__ es el "constructor"
    # Se ejecuta automáticamente al crear una nueva instancia de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad

    # Método para mostrar información
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto (instancia) de la clase
persona1 = Persona("Ana", 25)

# Usar un método del objeto
persona1.saludar()
