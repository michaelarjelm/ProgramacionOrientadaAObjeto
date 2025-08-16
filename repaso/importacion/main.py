# Importar módulos propios
import operaciones
import utilidades

# Usar funciones importadas
print(operaciones.sumar(5, 3))
print(operaciones.restar(10, 4))

print(utilidades.saludar("Ana"))
print(utilidades.despedir("Luis"))

# Importar librerías estándar
import math
import random

print("Raíz cuadrada de 16:", math.sqrt(16))
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))

# Importación con alias
import math as m
print("Valor de PI:", m.pi)

# Importar funciones específicas
from math import sqrt, pi
print("sqrt(25):", sqrt(25))
print("PI:", pi)
