# Representa una pregunta con su enunciado y respuesta.
class Pregunta:
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

# Gestiona una lista de preguntas para un examen.
class Examen:
    def __init__(self):
        self.preguntas = []

    def anadir_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
        print(f"Pregunta añadida: '{pregunta.enunciado}'")

    def listar_preguntas(self):
        if not self.preguntas:
            print("El examen no tiene preguntas.")
            return
        
        print("\n--- Preguntas del Examen ---")
        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"Pregunta {i}: {pregunta.enunciado} (Respuesta: {pregunta.respuesta_correcta})")

    def contar_total_preguntas(self):
        return len(self.preguntas)