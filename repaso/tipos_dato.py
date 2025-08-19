'''
nombre = input("Ingrese tu nombre: ")

edad = input("Ingresa tu edad: ")

#edadInt = int(edad)

print("El nombre del usuario es: ",nombre.upper())
print("La edad del usuario es: ",edad)
'''

import math


#variableUno=int(input("Ingresa el primer numero: "))
#variableDos=int(input("Ingresa el segundo numero: "))

# print("La suma de los numeros ingresados es: ", variableUno + variableDos )
# print("La suma de los numeros ingresados es: ", variableUno - variableDos )
# print("La suma de los numeros ingresados es: ", variableUno * variableDos )
# print("La suma de los numeros ingresados es: ", math.trunc(variableUno / variableDos) )

#alumnos=["Bastian", "Ruth", "Samuel", "Carlos", "Rolando"]

#print (alumnos)

#alumnos.append("Alondra")

#print (alumnos)

#print (alumnos[0])

#alumnos.append("Michael")

#print (alumnos)

#alumnos.remove("Michael")

#AlumnoEliminado = alumnos.pop(6)

#print("El alumno eliminado es: ", AlumnoEliminado)

#print (alumnos)

alumnos = [
    {"nombre":"Bastian","edad":18},
    {"nombre":"Michael","edad":37},
    {"nombre":"Joaquin","edad":19}
    
]

alumnos.append({"nombre":"etc", "edad":33})

#print(alumnos)

for alumno in alumnos:
    if alumno['edad']<20:
        print(f"El {alumno['nombre']} tiene {alumno['edad']} años")

contador = 0
while contador<10:
    print("contador: ", contador)
    contador+=1

def DameTuEdad():
    edad=input("¿Que edad tienes?")
    return edad
    
def saludar (nombre):
    print(f"Hello {nombre}")

edadTest = DameTuEdad()