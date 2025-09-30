from Clases.CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def retirar (self, monto):
        if monto <= 0:
            raise Exception ("El monto debe ser mayor a 0")
        if monto  # ncesitas el sobregiro?no
        #necesitas el sobre giro? Si
        #sobregiraste? saldo insuficiente y sobregiro insuficiente
        
        