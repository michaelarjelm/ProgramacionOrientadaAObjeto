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


class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo=saldo
        
    def depositar(self, monto):
        #Validamos que ningun chistoso diga que quiere depositar cero pesos
        if monto<=0:
            #Ejecuto la excepción y salgo del método
            raise Exception("El monto a depositar debe ser mayor a 0")  
        # al saldo le sumo el monto      
        self.__saldo+=monto
        
    def retirar(self, monto):
        #Validamos que ningun chistoso diga que quiere depositar cero pesos
        if monto<=0:
            #Ejecuto la excepción y salgo del método
            raise Exception("El monto a retirar debe ser mayor a 0")
            #Valido que el monto de retiro no sea mayor a mi saldo
        if monto>self.__saldo:
            #Ejecuto la excepción y salgo del método
            raise Exception("La pobreza te está respirando en la nuca")
        self.__saldo-=monto

    def mostrar_saldo(self):
        #Este metodo solo retorna como dato un saldo
        return self.__saldo
    
    def setSaldo(self,monto): 
        self.__saldo=monto
