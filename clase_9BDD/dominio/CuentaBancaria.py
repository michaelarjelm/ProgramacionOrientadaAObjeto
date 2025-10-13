class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def depositar(self, monto):
        #Validamos que ningun chistoso diga que quiere depositar cero pesos
        if monto<=0:
            #Ejecuto la excepción y salgo del método
            raise Exception("El monto a depositar debe ser mayor a 0")  
        # al saldo le sumo el monto      
        self.__saldo += monto
        
    def retirar(self, monto):
        #Validamos que ningun chistoso diga que quiere depositar cero pesos
        if monto <= 0:
            #Ejecuto la excepción y salgo del método
            raise Exception("El monto a retirar debe ser mayor a 0")
        #Valido que el monto de retiro no sea mayor a mi saldo
        if monto > self.__saldo:
            #Ejecuto la excepción y salgo del método
            raise Exception("La pobreza te está respirando en la nuca")
        self.__saldo -= monto

    def mostrar_saldo(self):
        #Este metodo solo retorna como dato un saldo
        return self.__saldo
    
    def setSaldo(self,monto): 
        self.__saldo = monto
        