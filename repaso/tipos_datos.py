# ----------------------------------------
# TIPOS DE DATOS Y VARIABLES EN PYTHON
# ----------------------------------------

# # 1️⃣ Variables: asignación y reglas
# #nombre = "Juan"  # String
# nombre = input("Ingresa tu nombre: ")
# #edad = 25        # Entero (int)
# edad=int(input("Ingresa tu edad: "))
# #altura = 1.75    # Decimal (float)
# altura = float(input("Ingresa tu altura: "))   # Decimal (float)
# es_estudiante = True  # Booleano

# print("Nombre:", nombre)
# print("Edad:", edad)
# print("Altura:", altura)
# print("Es estudiante:", es_estudiante)

# # ----------------------------------------
# # 2️⃣ Strings (cadenas de texto)
# texto = "Python es genial"
# print("\nTexto original:", texto)
# print("En mayúsculas:", texto.upper())
# print("En minúsculas:", texto.lower())
# print("Reemplazar 'genial' por 'increíble':", texto.replace("genial", "increíble"))
# print("Cantidad de caracteres:", len(texto))

# # ----------------------------------------
# # 3️⃣ Números: int y float
import math


a = 10
b = 3
#print("\nSuma:", a + b)
#print("Resta:", a - b)
#print("Multiplicación:", a * b)
#print("División:", a / b)     # Resultado con decimales
#print("División:", round(a / b,2))     # Resultado con decimales limitados
#print("División entera:", a // b)  # Resultado sin decimales
#print("Módulo (resto):", a % b)
##print("Potencia:", a ** b)#Potencia al cuadrado
##print("Potencia:", int(math.pow(a,4)))#Calcular potencia mayor a 2

# ----------------------------------------
# 4️⃣ Booleanos
# tiene_permiso = True
# edad=18
# es_mayor = edad >= 18
# print("\n¿Tiene permiso?:", tiene_permiso)
# print("¿Es mayor de edad?:", es_mayor)
# print("¿Es mayor de edad?:", "si"if es_mayor else "No")

# ----------------------------------------
# # 5️⃣ Listas (mutables, ordenadas)
# colores = ["rojo", "verde", "azul"]
# print("\nLista de colores:", colores)
# colores.append("amarillo")  # Agregar elemento
# print("Lista después de agregar amarillo:", colores)
# print("Primer color:", colores[0])  # Acceso por índice
# colores.remove("amarillo")
# print("\nLista de colores:", colores)
# eliminado = colores.pop(1)  # Elimina el elemento en posición 1
# print(colores, "Elemento eliminado:", eliminado)


# Diccionario principal de personas
# Lista de personas
# personas = [
#     {"nombre": "Ana", "edad": 25},
#     {"nombre": "Luis", "edad": 30},
#     {"nombre": "María", "edad": 22}
# ]

# # 📋 READ: Mostrar todas las personas
# print("\n📋 Personas registradas:")
# for persona in personas:
#     print(f"- {persona['nombre']} tiene {persona['edad']} años")

# # 🆕 CREATE: Agregar una nueva persona
# nueva_persona = {"nombre": "Pedro", "edad": 27}
# personas.append(nueva_persona)
# print("\n✅ Pedro fue agregado.")

# # 🔄 UPDATE: Modificar edad de una persona (ej. Luis)
# for persona in personas:
#     if persona["nombre"] == "Luis":
#         persona["edad"] = 31
#         print(f"\n🔄 Edad actualizada de Luis: {persona['edad']} años")

# # ❌ DELETE: Eliminar a Ana
# personas = [p for p in personas if p["nombre"] != "Ana"]
# print("\n❌ Ana fue eliminada.")

# # Mostrar estado final
# print("\n📌 Estado final de la lista:")
# for persona in personas:
#     print(f"- {persona['nombre']}: {persona['edad']} años")



# ----------------------------------------
# 8️⃣ Sets (sin orden, sin duplicados)

# 🔹 CREATE: Crear un set de frutas
# frutas = {"manzana", "pera", "uva", "pera"}  # 'pera' duplicada será ignorada

# 🔹 READ: Mostrar todas las frutas
# print("\n📋 Frutas registradas (sin duplicados):")
# for fruta in frutas:
#     print("-", fruta)

# 🔹 UPDATE: No existe como tal en sets, pero puedes eliminar y volver a agregar
# Ejemplo: Cambiar "uva" por "sandía"
# if "uva" in frutas:
#     frutas.remove("uva")
#     frutas.add("sandía")
#     print("\n🔄 'uva' fue reemplazada por 'sandía'")

# 🔹 DELETE: Eliminar una fruta
# frutas.discard("pera")  # No lanza error si no existe
# print("\n❌ 'pera' fue eliminada.")

# 🔹 CREATE: Agregar una nueva fruta
# frutas.add("naranja")
# print("\n✅ 'naranja' fue agregada.")

# Estado final
# print("\n📌 Estado final del set de frutas:")
# for fruta in frutas:
#     print("-", fruta)


# # ----------------------------------------
# # 9️⃣ Conversión de tipos
# numero_str = "100"
# numero_int = int(numero_str)
# print("\nString original:", numero_str, type(numero_str))
# print("Convertido a entero:", numero_int, type(numero_int))
# print("Convertido a float:", float(numero_int), type(float(numero_int)))
# print("Convertido a string:", str(numero_int), type(str(numero_int)))

# # ----------------------------------------
# # 💡 Nota: Python es de tipado dinámico
# variable = 5
# print("\nVariable con valor entero:", variable, type(variable))
# variable = "Ahora soy un texto"
# print("Variable con valor string:", variable, type(variable))
