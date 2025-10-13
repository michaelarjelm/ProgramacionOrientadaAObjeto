# class CuentaBancaria:
#     def __init__(self, saldo):
#         self.__saldo = saldo
        
#     def depositar(self, monto):
#         if monto >= 1:
#             self.__saldo += monto
#         else:
#             return "Monto invalido"
    
#     def retirar(self, monto):
#         if monto > 0:
#             if self.__saldo - monto >= 0:
#                 self.__saldo -= monto
#             else:
#                 return "Saldo insuficiente"
#         else:
#             return "monto invalido"
    
#     def mostrar_saldo(self):
#         return self.__saldo
    
#     def _actualizar_saldo(self, nuevo_saldo):
#         if nuevo_saldo > 0:
#             self.__saldo = nuevo_saldo
    
    
# class CuentaAhorro(CuentaBancaria):
#     # No necesita contructor porque lo hereda del padre
    
#     def mostrar_saldo(self):
#         saldo = super().mostrar_saldo() * 1.02
#         self._actualizar_saldo(saldo)
#         return super().mostrar_saldo()
        
        
# class CuentaCorriente(CuentaBancaria):
#     # No necesita contructor porque lo hereda del padre
    
#     def retirar(self, monto):
#         if monto > 0:
#             if self.mostrar_saldo() - monto >= -500:
#                 self.__saldo -= monto
#             else:
#                 return "Saldo insuficiente"
#         else:
#             return "monto invalido"


# cuentas = [CuentaBancaria(1000), CuentaAhorro(1000), CuentaCorriente(1000)]


# for cuenta in cuentas:
#     print(cuenta.mostrar_saldo())

# print("-----------")
# a = CuentaAhorro(1000)
# print(a.retirar(1300))
# print(a.mostrar_saldo())
# print(a.mostrar_saldo())
