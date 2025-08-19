# import math
# # nombre = input("Ingresa tu nombre: ")
# # edad = input("Ingresa tu edad: ")
# # #edadInt=int(edad) convierto el string recibido a un integer

# # print("El nombre del usuario es: ", nombre.upper()) #convierto a mayúsculas con el método .upper
# # print("La edad del usuario es: ",edad)

# variableUno=int(input("Ingresa el primer número: "))
# variableDos=int(input("Ingresa el segundo número: "))

# print("La suma de los números ingresados es: ",variableUno+variableDos) #suma
# print("La suma de los números ingresados es: ",variableUno-variableDos) #resta
# print("La suma de los números ingresados es: ",variableUno*variableDos) #multiplicación
# print("La suma de los números ingresados es: ",variableUno/variableDos) #división
# print("La suma de los números ingresados es: ",variableUno//variableDos) #división entero
# print("La suma de los números ingresados es: ", round(variableUno+variableDos,2)) #redondear
# print("La suma de los números ingresados es: ", math.trunc(variableUno+variableDos)) #truncar

# alumnos=["Bastian", "Ruth", "Samuel", "Carlos", "Rolando"]
# #print(alumnos)

# alumnos.append("Alondra") #añadimos un nombre más
# print(alumnos)
# print(alumnos[0])

# alumnos.remove("Alondra") #elimina por NOMBRE

# alumnoEliminado=alumnos.pop(2) #Eliminar por índice y almacenar en otra lista
# print("El alumno eliminado es ", alumnoEliminado)
# print(alumnos)

## HAGAMOS UN DICCIONARIO ##
# alumnos = [
#     {"nombre":"Bastian", "edad":18},
#     {"nombre":"Michael", "edad":37},
#     {"nombre":"Joaquin", "edad":19},
# ]

# alumnos.append({"nombre":"etc","edad":33})
# #print(alumnos)

# for alumno in alumnos: #con la identación le estoy indicando lo que quiero recorrer
#     if alumno["edad"]>20:
#         print(f"{alumno["nombre"]} tiene {alumno["edad"]} años")

# contador=0
# while contador<3:
#     print("Contador: ", contador)
#     contador+=1

def saludar(nombre): #metodos (los métodos con parámetros meten algo dentro del paréntesis)
    print(f"Hello {nombre}")
    