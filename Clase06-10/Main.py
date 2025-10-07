from Clases.PagoTarjeta import PagoTarjeta
from Clases.PagoPaypal import PagoPaypal
from Clases.PagoEfectivo import PagoEfectivo

pagos = [PagoTarjeta(), PagoPaypal(), PagoEfectivo()]

for pago in pagos:
    print(f"{pago.procesar(1000)}")