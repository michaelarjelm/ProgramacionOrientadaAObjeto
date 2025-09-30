class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
     
    def mostrarSaldo (self):
        return self.__saldo
    
    def depositarMonto (self, monto):
        if monto <=0:
            raise Exception ("El monto debe ser positivo")
        else:
            self.__saldo += monto
            
    def retirarMonto (self, monto):
        if monto <=0:
            raise Exception ("El monto a retirar debe ser mayor a 0")
        if  monto > self.__saldo:
            raise Exception ("Estás bien pobre")
        self.__saldo -= monto
    
    
        