from pago_abstracta import Pago


class PagoTarjeta(Pago):
    def procesar(self, monto):
        return f"Procesando {monto} con tarjeta bancaria"  