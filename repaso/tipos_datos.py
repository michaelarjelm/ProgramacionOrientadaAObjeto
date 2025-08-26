# nombre=input("Ingresa tu nombre: ")

# edad=input("ingresa tu edad: ")

# #edadInt=int(edad)

# print("El nombre del usuario es: ",nombre.upper())
# print("La edad del usuario es: ",edad)

# import math

# from POO.ejercicios_poo import Circulo


# variableUno=int(input("Ingresa el primer número: "))
# variableDos=int(input("Ingresa el segundo número: "))


# print("La suma de los números ingresados es: ", variableUno + variableDos )
# print("La suma de los números ingresados es: ", variableUno - variableDos )
# print("La suma de los números ingresados es: ", variableUno * variableDos )
# print("La suma de los números ingresados es: ", math.trunc(variableUno / variableDos,2) )

# alumnos=["Bastian", "Ruth", "Samuel", "Carlos", "Rolando"]

# #print (alumnos)

# alumnos.append("Alondra")

# print (alumnos)

# print(alumnos[0])

# alumnos.append("Michael")

# print (alumnos)

# alumnoEliminado=alumnos.pop(6)

# print("El alumno Eliminado es ", alumnoEliminado)


# print (alumnos)


# alumnos = [
#     {"nombre":"Bastian","edad":18},
#     {"nombre":"Michael","edad":37},
#     {"nombre":"Joaquin","edad":19}
# ]

# alumnos.append({"nombre":"etc", "edad":33})
# ##print (alumnos)

# for alumno in alumnos:
#     if (alumno['edad']<20 &alumno['edad']>20):
#         print(f"El {alumno['nombre']} tiene {alumno['edad']} años")

# contador=0
# while contador<10:
#     print("Contador: ", contador)
#     contador+=1

# def DameTuEdad():
#     edad=input("¿Que edad tienes?")
#     return int(edad)


# circulo = Circulo(5) #le estoy pasando los parámetros al constructor
# area = circulo.area()
# print("El área es: ", area)


from ejercicioPersona.persona import Persona

presentarse1 = Persona("Javiera",30)
presentarse2 = Persona("Andrea",28)

presentarse1.presentarse()
presentarse2.presentarse()