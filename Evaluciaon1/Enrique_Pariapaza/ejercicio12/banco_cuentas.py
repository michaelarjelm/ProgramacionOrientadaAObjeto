# Representa una cuenta bancaria con su titular y saldo.
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

# Gestiona una colección de cuentas bancarias.
class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"Cuenta de '{cuenta.titular}' abierta con un saldo de ${cuenta.saldo}.")

    def buscar_cuenta_por_titular(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular.lower() == titular.lower():
                return cuenta
        return None

    def transferir_dinero(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta_por_titular(titular_origen)
        cuenta_destino = self.buscar_cuenta_por_titular(titular_destino)

        if cuenta_origen and cuenta_destino:
            if cuenta_origen.saldo >= monto:
                cuenta_origen.saldo -= monto
                cuenta_destino.saldo += monto
                print(f"Transferencia de ${monto} de '{titular_origen}' a '{titular_destino}' realizada.")
                return True
            else:
                print(f"Saldo insuficiente en la cuenta de '{titular_origen}'.")
                return False
        else:
            print("Una o ambas cuentas no fueron encontradas.")
            return False

    def mostrar_estado_cuentas(self):
        if not self.cuentas:
            print("No hay cuentas registradas en el banco.")
            return
        
        print("\n--- Estado de las Cuentas ---")
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}, Saldo: ${cuenta.saldo}")