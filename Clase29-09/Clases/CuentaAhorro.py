from CuentaBancaria import CuentaBancaria
    
class CuentaAhorro (CuentaBancaria):
    interes = 1.02
    def mostrarSaldo(self):
        return self.interes* super().mostrarSaldo()