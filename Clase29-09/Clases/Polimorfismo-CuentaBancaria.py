#POLIMORFISMO. Un método que este en diferentes clases, que tiene el mismo nombre y puede o no ser heredable, hace que se comporte diferente. 
# Pasa una clase (como objeto) como un atributo. En vez de (self) hay que usar (obj)

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
     
    def mostrarSaldo (self):
        return self.__saldo
    
    def depositarMonto (self, cantidad):
        if cantidad >=0:
            self.__saldo += cantidad
        else:
            print (f"La cantidad ingresada no es válida")
     
    def retirarMonto (self, cantidad):
        if cantidad >0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print (f"No es posible retirar el monto ingresado")
    
class CuentaAhorro (CuentaBancaria):
    def SaldoConInterés (self):
        saldoBase = self.mostrarSaldo()
        interesGanado = saldoBase * 0,2
        return saldoBase + interesGanado
    
class CuentaCorriente (CuentaBancaria):
    def sobreGiro (self, giro):
        saldoActual = self.mostrarSaldo()
        print (f"La cuenta")

CuentasBancarias = [CuentaAhorro(1000), CuentaCorriente(500) ]
for c in CuentasBancarias:
    print (c.mostrarSaldo())