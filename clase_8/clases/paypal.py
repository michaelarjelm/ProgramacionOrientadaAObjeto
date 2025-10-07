from pago_abstracta import Pago


class PagoPaypal(Pago):
    def procesar(self, monto):
        return f"Procesando {monto} con PayPal"