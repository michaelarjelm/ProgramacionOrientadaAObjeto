# Representa un empleado con su nombre y sueldo.
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

# Gestiona una lista de empleados para una empresa.
class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado '{empleado.nombre}' contratado.")

    def listar_empleados(self):
        if not self.empleados:
            print("La empresa no tiene empleados.")
            return
        
        print("\n--- Listado de Empleados ---")
        for empleado in self.empleados:
            print(f"Nombre: {empleado.nombre}, Sueldo: ${empleado.sueldo}")
    
    def calcular_gasto_total_sueldos(self):
        total_sueldos = sum(empleado.sueldo for empleado in self.empleados)
        return total_sueldos