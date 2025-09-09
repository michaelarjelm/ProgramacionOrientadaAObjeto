from ejercicio4.clases.tienda import Tienda
from ejercicio3.clases.cuentaBancaria import CuentaBancaria
from ejercicio2.clases.coche import Coche
from ejercicio1.clases.Persona import Persona
from clases.circulo import Circulo
from ejercicio4.clases.producto import Producto


#mi_circulo = Circulo(5)

#print ("El área del circulo es: ", mi_circulo.calcularArea())

# #Ejercicio1

# persona1 = Persona("Ana", 25)
# persona2 = Persona("Luis", 30)

# # Llamar al método
# persona1.presentarse()
# persona2.presentarse()

#FinEjercicio1

#Ejercicio 2 coche
# Crear un coche
mi_coche = Coche("Toyota", "Corolla")

# Conducir 30 km
mi_coche.conducir(30)

# Recargar 20
mi_coche.recargar(20)

# Estado final
print("Combustible final:", mi_coche.combustible)

######Ejercicio 3
cuenta = CuentaBancaria("Carlos")   # saldo inicia en 0
cuenta.mostrar_saldo()

cuenta.depositar(500)               # +500
cuenta.retirar(600)                 # fondos insuficientes
cuenta.retirar(300)                 # -300
cuenta.mostrar_saldo()              # saldo final: 200

######Fin Ejercicio 3

##Ejercicio4

# Crear productos
p1 = Producto("Laptop", 1200, 2)
p2 = Producto("Mouse", 25, 3)
p3 = Producto("Teclado", 45, 1)

# Crear tienda y agregar productos
tienda = Tienda("Tech Store")
tienda.agregar_producto(p1)
tienda.agregar_producto(p2)
tienda.agregar_producto(p3)

# Mostrar ticket y total
tienda.mostrar_ticket()
# O solo:
# print("Total a pagar:", tienda.calcular_total())



