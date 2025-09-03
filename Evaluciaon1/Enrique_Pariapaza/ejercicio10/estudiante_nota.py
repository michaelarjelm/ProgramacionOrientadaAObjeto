# Representa la calificación de una materia.
class Nota:
    def __init__(self, asignatura, calificacion):
        self.asignatura = asignatura
        self.calificacion = calificacion

# Modela a un estudiante y sus calificaciones.
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def anadir_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota de '{nota.asignatura}' añadida para {self.nombre}.")

    def calcular_promedio(self):
        if not self.notas:
            return 0
        
        total_calificaciones = sum(nota.calificacion for nota in self.notas)
        return total_calificaciones / len(self.notas)

    def mostrar_calificaciones(self):
        if not self.notas:
            print(f"{self.nombre} no tiene notas registradas.")
            return
        
        print(f"\n--- Calificaciones de {self.nombre} ---")
        for nota in self.notas:
            print(f"Asignatura: {nota.asignatura}, Calificación: {nota.calificacion}")