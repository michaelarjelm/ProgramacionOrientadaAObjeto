class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a depositar debe ser positiva.")
            return
        self.saldo += cantidad
        print(f"Depósito de {cantidad}. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
            return
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
            return
        self.saldo -= cantidad
        print(f"Retiro de {cantidad}. Saldo actual: {self.saldo}")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: {self.saldo}")
