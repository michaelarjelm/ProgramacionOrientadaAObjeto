# Modela una mesa de restaurante con su número, capacidad y estado.
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "libre"

# Gestiona la administración de mesas y reservas de un restaurante.
class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        print(f"Mesa {mesa.numero} con capacidad para {mesa.capacidad} agregada.")

    def reservar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if mesa.estado == "libre":
                    mesa.estado = "ocupada"
                    print(f"Mesa {numero_mesa} reservada con éxito.")
                    return True
                else:
                    print(f"Mesa {numero_mesa} ya está ocupada.")
                    return False
        print(f"Mesa {numero_mesa} no encontrada.")
        return False

    def liberar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if mesa.estado == "ocupada":
                    mesa.estado = "libre"
                    print(f"Mesa {numero_mesa} liberada.")
                    return True
                else:
                    print(f"Mesa {numero_mesa} ya estaba libre.")
                    return False
        print(f"Mesa {numero_mesa} no encontrada.")
        return False

    def mostrar_estado_mesas(self):
        if not self.mesas:
            print("No hay mesas registradas.")
            return
        
        print("\n--- Estado de las Mesas ---")
        for mesa in self.mesas:
            print(f"Mesa {mesa.numero} (Capacidad: {mesa.capacidad}): {mesa.estado}")