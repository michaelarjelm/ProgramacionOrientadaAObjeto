# # # nombre=input("ingresa tu nombre: ")

# # edad=input("ingresa tu edad: ")

# # #edadint=int(edad)

# # print("el nombre del usuario es :",nombre.upper())
# # # print("la edad del usuario es :",edad)

# import math


# variableUno=int(input("ingresa el primer numero: "))
# variableDos=int(input("ingresa el segundo numero: "))

# # print("la suma de los numeros ingresados es: ", variableUno + variableDos )
# # print("la suma de los numeros ingresados es: ", variableUno - variableDos )
# # print("la suma de los numeros ingresados es: ", variableUno * variableDos )
# print("la suma de los numeros ingresados es: ", math.trunc(variableUno / variableDos,2))


# # alumnos=["bastian", "ruth" ,"samuel", "carlos", "rolando"]

# # print (alumnos)

# # alumnos.append("alondra")

# # # print (alumnos)

# # # print(alumnos[0])

# # alumnos.append("michael")

# # print(alumnos)

# # alumnoEliminado=alumnos.pop(6)

# # print ("el alumno eliminado es ", alumnoEliminado)

# # print(alumnos)

# alumnos = [
#     {"nombre" : "bastian" , "edad" :18},
#     {"nombre" : "michael" , "edad" :37},
#     {"nombre" : "joaquin" , "edad" :19},
# ]

# alumnos.append({"nombre" : "etc","edad":33})
# # print (alumnos)

# for alumno in alumnos:
#     if (alumno ["edad"]<20:
#         print(f"El{alumno["nombre"]} tiene {alumno["edad"]} años")
        
# contador=0
# while contador<10:
#     print("contador: ", contador) 
#     contador+=1       

def DameTuEdad():
   edad=input ("¿que edad tienes?") 
   return int (edad) 

def saludar(DameTuEdad):
    print(f"hello {nombre}")  
    
edadPrueba=DameTuEdad()
      