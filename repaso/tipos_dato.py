# Nombre="Dayane" #esto es ina cadena
# nombre=input("ingresar tu nombre")#pedir info al usuario
# edad=input("ingresa tu edad")
# #edadInt=int(edad)#tranforma a entero y ayuda a llamar 

# print("El nombre del usuario es: ", nombre.upper())
# print("La edad del usuario es: ",edad)...


# import math


# variableUno=int(input("Ingresa el primer numero: "))
# variableDos=int(input("Ingresa el segundo numero: "))


# print("La suma de los numeri ingresados es: ",variableUno + variableDos)
# print("La suma de los numeri ingresados es: ",variableUno - variableDos)
# print("La suma de los numeri ingresados es: ",variableUno * variableDos)
# print("La suma de los numeri ingresados es: ",variableUno / variableDos)
#print("La suma de los numeri ingresados es: ",variableUno // variableDos) # con // te da el numero entero sin decimal
#print("La suma de los numeri ingresados es: ",round(variableUno / variableDos,2))#redondea los decimales y con la coordenada se asigna los decinmales que muestra
#print("La suma de los numeri ingresados es: ",math.trunc(variableUno / variableDos,2))#con math puedes truncar, sacar potencias y se agrega mediante una biblioteca
#SePuedeTruncar=False

# alumnos=["Bastian","Ruth","Samuel","Carlos","Rolando"]
# #print (alumnos)
# alumnos.append("Alondra")
# # print (alumnos)
# # print (alumno[0])

# alumnos.append("Michael")
# print (alumnos)
# #alumnos.pop(6)#pop siverve para eliminar variables
# alumnoEliminado=alumnos.pop(6)
# print (alumnos)
# print ("El alumno eliminado es: ",alumnoEliminado)
# print (alumnos)

# alumnos = [
#     {"nombre":"Bastian","edad":18},
#     {"nombre":"Michael","edad":37},
#     {"nombre":"Joaquin","edad":19}
# ]
# alumnos.append({"nombre":"etc","edad":33})
# #print (alumnos)
# for alumno in alumnos:
#     if (alumno['edad']<20 &alumno['edad']>20):
#         print(f"El {alumno['nombre']} tiene {alumno['edad']} años")
    
# contador=0
# while contador<10:
#     print ("contador: ",contador)   
#     contador+=1
  
def DameTuEdad():
    edad=input("¿Que edad tienes?")
    return int(edad)

edadPrueba=DameTuEdad()    
# def saludar(nombre):#variables y parametros, existen con y sin. definicion de variables
#     print(f"Hello {nombre}")
    
# Saludar("Javiera")