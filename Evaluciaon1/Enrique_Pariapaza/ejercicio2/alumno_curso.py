# Esta clase representa un alumno con su nombre.
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        
# Esta clase gestiona un curso y la lista de sus alumnos.
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
        
    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)
        print(f"'{alumno.nombre}' ha sido inscrito en el curso de '{self.nombre}'.")
        
    def remover_alumno(self, nombre_alumno):
        for alumno in self.alumnos:
            if alumno.nombre == nombre_alumno:
                self.alumnos.remove(alumno)
                print(f"'{nombre_alumno}' ha sido removido del curso de '{self.nombre}'.")
                return
        print(f"'{nombre_alumno}' no se encuentra en el curso.")
        
    def listar_alumnos(self):
        if not self.alumnos:
            print(f"El curso de '{self.nombre}' no tiene alumnos inscritos.")
            return
        
        print(f"\n--- Alumnos inscritos en el curso de '{self.nombre}' ---")
        for alumno in self.alumnos:
            print(f"- {alumno.nombre}")