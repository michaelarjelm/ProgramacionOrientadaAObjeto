# nombre = input("Ingresa un nombre: ")
# edad = int(input("Ingresa tu edad: "))
# print("El nombre del usuario es:", nombre.upper())
# print("La edad del usuario es:", edad)
#------ ctrl+k ctrl+c para comentar todo lo seleccionado
#------ ctrl+k ctrl+u para deshacer

# import math


# variable_uno = int(input("Ingresa el primer numero: "))
# variable_dos = int(input("Ingresa el segundo numero: "))

# print("La suma de los numeros es:", round(variable_uno / variable_dos)) #ver como truncar 2 decimales

#------ Listas

# alumnos = ["Bastian", "Ruth", "Samuel", "Carlos", "Rolando"]
# alumnos.append("Alondra")
# print(alumnos)

# alumnos.append("Michael")
# print(alumnos)  

# alumno_eliminado = alumnos.pop(6)
# print("El alumno eliminado es", alumno_eliminado)
# print(alumnos)

#----- Diccionarios

# alumnos = [
#     {"nombre":"Bastian","edad":18},
#     {"nombre":"Michael","edad":37},
#     {"nombre":"Joaquin","edad":19}
# ]

# for alumno in alumnos:
#     print(f"El alumno {alumno['nombre']} tiene {alumno['edad']} años")
    
# alumnos.append({"nombre" : "etc", "edad" : 33})
# print("-----")

# for alumno in alumnos:
#     if alumno["edad"] > 20:
#         print(f"El alumno {alumno['nombre']} tiene {alumno['edad']} años")


#def saludar(nombre): #funcion o metodo con parametro
#def saludar(): #funcion o metodo sin parametro

def saludar(nombre):
    print(f"Hello {nombre}")
    
saludar("Javiera")   

def DameTuEdad():
    edad = ("Que edad tienes? ")
    return int(edad)

        