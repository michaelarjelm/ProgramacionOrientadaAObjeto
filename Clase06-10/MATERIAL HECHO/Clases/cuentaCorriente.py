#📌 Ejercicio 1 – Cuentas bancarias
# Crea una clase base CuentaBancaria con:
# Atributo privado __saldo. Done!
# Métodos depositar(monto) y retirar(monto) con validación (no permitir montos negativos, 
# ni saldo insuficiente).Done
# Método mostrar_saldo() que devuelve el saldo.
# Subclases:
# CuentaAhorro → gana un interés de 2% cuando se consulta el saldo. 
# CuentaCorriente → permite sobregiro de hasta -500.
# 👉 Recorre una lista de cuentas y llama a mostrar_saldo() en cada una, mostrando polimorfismo.


# 1000 900 Todo ok=>done
# 1000 1200 Todo ok pero con sobregiro
# 1000 1600 Ehh te pasaste! tu sobregiro maximo es de 500 

from Clases.cuentaBancaria import CuentaBancaria # type: ignore

class CuentaCorriente(CuentaBancaria):
    LIMITE_SOBREGIRO=500
    def retirar(self, monto):
        if monto<=0:
            raise Exception("El monto a retirar debe ser mayor a 0")
        if monto<=super().mostrar_saldo():
            super().retirar(monto)
        else:
            if monto > super().mostrar_saldo():#V o F#
                if monto > (self.mostrar_saldo()+self.LIMITE_SOBREGIRO):
                    raise Exception("Sobrepasaste tu sobregiro")
                else:
                    return self.setSaldo(super().mostrar_saldo()-monto)