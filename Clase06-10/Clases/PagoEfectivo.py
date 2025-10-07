from Clases.Pago import Pago

class PagoEfectivo(Pago):
    def procesar(self, monto):
        return f"Procesando {monto} con pago en efectivo."