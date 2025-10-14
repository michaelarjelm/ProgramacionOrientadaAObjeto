from .CuentaBancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):
    LIMITE_SOBREGIRO = 500
    def retirar(self, monto):
        if monto <= 0:
            raise Exception("El monto a retirar debe ser mayor a 0")
        if monto<=super().mostrar_saldo():
            super().retirar(monto)
        else:
            if monto > super().mostrar_saldo():#V o F#
                if monto > (self.mostrar_saldo() + self.LIMITE_SOBREGIRO):
                    raise Exception("Sobrepasaste tu sobregiro")
                else:
                    return self.setSaldo(super().mostrar_saldo() - monto)
