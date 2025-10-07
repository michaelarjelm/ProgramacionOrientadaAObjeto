from clases.efectivo import PagoEfectivo
from clases.pagoTarjeta import PagoTarjeta
from clases.paypal import PagoPaypal


pagos = [PagoTarjeta(), PagoPaypal(), PagoEfectivo()]

for pago in pagos:
    print(f"{pago.procesar(1000)}")
    
