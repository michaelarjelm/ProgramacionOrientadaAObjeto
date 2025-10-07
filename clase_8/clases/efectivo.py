from pago_abstracta import Pago


class PagoEfectivo(Pago):
    def procesarPago(self, monto):
        return f"Procesando {monto} con efectivo"  