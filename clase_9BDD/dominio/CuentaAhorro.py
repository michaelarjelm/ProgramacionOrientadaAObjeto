from .CuentaBancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    INTERES = 1.02
    def mostrar_saldo(self):
        return self.INTERES * super().mostrar_saldo()