# # nombre = input("ingresa tu nombre: ")

# # edad = input ("ingresa tu edad: ")

# # #edadINT = int(edad)

# # print("el nombre del usuario es: ",nombre.upper())
# # print("la edad del usuario es: ",edad)

# import math


# Variableuno=int(input("Ingrese el primer numero: "))
# Variabledos=int(input("Ingrese segundo numero: "))

# # print("la suma de los numeros ingresados es: ", Variableuno + Variabledos)
# # print("la suma de los numeros ingresados es: ", Variableuno * Variabledos)
# # print("la suma de los numeros ingresados es: ", Variableuno - Variabledos)
# print(f"la suma de los numeros ingresados es: , {Variableuno / Variabledos:.2f}")

# alumnos=["Bastian","Ruth","Samuel","carlos","Rolando"]

# #print (almunos)

# alumnos.append("Alondra")

# print (alumnos)

# print(alumnos=[0])

# alumnos.append("Michael")

# print (alumnos)
# alumnoEliminados=alumnos.pop(6)
# print("El alumno eliminado es: ", alumnoEliminados)

# print (alumnos)

alumnos= [
   {"nombre":"Bastian","edad":18},
   {"nombre":"Michael","edad":37},
   {"nombre":"joaquin","edad":19},
 
]

alumnos.append({"nombre":"etc", "edad" :33})
print (alumnos)
for alumno in alumnos:
    if alumno["edad"]>20:
      print(f"el{alumno["nombre"]} tiene {alumno["edad"]} años")
     
# def saludar(nombre):
#     print("Hello {nombre}")
    
