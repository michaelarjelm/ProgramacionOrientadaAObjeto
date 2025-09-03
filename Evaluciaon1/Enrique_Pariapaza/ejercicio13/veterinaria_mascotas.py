# Modela los datos de una mascota (nombre, especie, edad).
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

# Administra un registro de mascotas.
class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota '{mascota.nombre}' registrada.")

    def buscar_por_nombre(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                return mascota
        return None

    def listar_todas(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return
        
        print("\n--- Listado de Mascotas ---")
        for mascota in self.mascotas:
            print(f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad}")

    def calcular_edad_promedio(self):
        if not self.mascotas:
            return 0
        
        total_edad = sum(mascota.edad for mascota in self.mascotas)
        return total_edad / len(self.mascotas)