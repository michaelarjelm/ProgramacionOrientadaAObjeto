#📌 Ejercicio 1 – Cuentas bancarias
# Crea una clase base CuentaBancaria con:
# Atributo privado __saldo. Done!
# Métodos depositar(monto) y retirar(monto) con validación (no permitir montos negativos, 
# ni saldo insuficiente).Done
# Método mostrar_saldo() que devuelve el saldo.
# Subclases:
# CuentaAhorro → gana un interés de 2% cuando se consulta el saldo. Done
# CuentaCorriente → permite sobregiro de hasta -500.
# 👉 Recorre una lista de cuentas y llama a mostrar_saldo() en cada una, mostrando polimorfismo.

from Clases.cuentaBancaria import CuentaBancaria
from Clases.cuentaCorriente import CuentaCorriente

cuentas : list[CuentaBancaria] = [
    CuentaCorriente(1000)
]

for c in cuentas:
    print(f"{c.__class__.__name__}:$ {c.mostrar_saldo()}")
    c.retirar(1600)
    print(f"{c.__class__.__name__}:$ {c.mostrar_saldo()}")