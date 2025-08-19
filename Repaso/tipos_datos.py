#nombre=input("Ingresa tu nombre: ")

#edad=input("Ingresa tu edad: ")

#edadInt=int(edad)

#print("El nombre del usuario es: ",nombre.upper())
#print("La edad del usuario es: ",edad)

import math


# variableUno=int(input("Ingresa el primer numero: "))
# variableDos=int(input("Ingresa el segundo numero: "))


# # print("La suma de los numeros ingresados es: ", variableUno + variableDos )
# # print("La suma de los numeros ingresados es: ", variableUno - variableDos )
# # print("La suma de los numeros ingresados es: ", variableUno * variableDos ) 
# print("La suma de los numeros ingresados es: ", math.trunc(variableUno / variableDos,))

# alumnos=["Bastian", "Ruth", "Samuel", "Carlos", "Rolando"]

# #print (alumnos)

# alumnos.append("Alondra")

# print (alumnos)

# printer(alumnos[0])

# alumnos.append("Michael")

# print (alumnos)

# alumnoEliminado=alumnos.pop(6)

# print ("El alumno Eliminado es ", alumnoEliminado)


# print (alumnos)


alumnos = [
    {"nombre":"Bastian","edad":18},
    {"nombre":"Michael","edad":37},
    {"nombre":"Joaquin","edad":19}
]

alumnos.append({"nombre":"etc","edad":33})
##print (alumnos)

for alumno in alumnos:
    if (alumno['edad']<20 &alumno['edad']>36):
         print(f"El {alumno['nombre']} tiene {alumno['edad']} años")