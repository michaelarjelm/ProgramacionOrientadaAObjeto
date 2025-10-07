from Clases.Pago import Pago

class PagoPaypal(Pago):
    def procesar(self, monto):
        return f"Procesando {monto} con Paypal."