# nombre = input ("Ingresa tu nombre:") #esto es pedirle al usario ingrese una información
# edad = input("Ingresa tu edad:") #se le pide al usario su edad, esta se guarda como string
# #edadInt=int(edad) #se asigna una nueva variable para volver entero la variable anterior a través de int

# print("El nombre del usuario es:", nombre.upper())
# print("La edad del usuario es:", edad)

import math


# variableUno=int(input("Ingresa el primer número:"))
# variableDos=int(input("Ingresa el segundo número:"))

# print("La suma de los números ingresados es:", variableUno + variableDos)
# print("La suma de los números ingresados es:", variableUno - variableDos)
# print("La suma de los números ingresados es:", variableUno * variableDos)
# print("La suma de los números ingresados es:", variableUno / variableDos)
# print("La suma de los números ingresados es:", variableUno // variableDos) #devuelve la division en entero
# print("La suma de los números ingresados es:", round(variableUno / variableDos, 2)) #redondea los decimales y con la coordenada se asigna los decimales que muestra
# print("La suma de los números ingresados es:", math.trunc(variableUno / variableDos)) #con esto permite truncar por medio de la biblioteca math
#TAREA PARA LA CASA: truncar con decimales#

#sePuedeTruncar=False

# alumnos=["Javiera", "Dayan", "Andrea", "Bastian", "Ruth"]
# print (alumnos)
# alumnos.append("Alondra")
# print (alumnos)
# print (alumnos[0])
# alumnos.append("Michael")
# print (alumnos)
# alumnos.remove("Michael") #Con esto se remueve el string
# alumnos.pop(6) #Con esto se remueve con el índice
# alumnoEliminado=alumnos.pop(6) #Acá creamos una lista de los posibles alumnos que se van eliminando
# print ("El alumno eliminado es:", alumnoEliminado)
# print (alumnos)

# alumnos = [
#     {"nombre":"Bastian", "edad":18},
#     {"nombre":"Michael", "edad":37},
#     {"nombre":"Joaquin", "edad":19}
# ]

# alumnos.append({"nombre":"etc", "edad" :33})

# for alumno in alumnos:
#     if (alumno['edad'])>20:
#         print(f"El {alumno['nombre']} tiene {alumno['edad']} años")
        
# contador=0
# while contador<10:
#     print("Contador: ", contador)
#     contador+=1
 
def DameTuEdad():
    edad=input("¿Qué edad tienes?")
    return int(edad)
    
# def saludar(): #definición de método/de función, con parantesis se llaman parámetros, con parentesis vacios es sin param
#     print(f"Hello {nombre}")
    
edadPrueba=DameTuEdad()
    