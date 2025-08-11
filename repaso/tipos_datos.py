# ----------------------------------------
# TIPOS DE DATOS Y VARIABLES EN PYTHON
# ----------------------------------------

# 1️⃣ Variables: asignación y reglas
nombre = "Juan"  # String
edad = 25        # Entero (int)
altura = 1.75    # Decimal (float)
es_estudiante = True  # Booleano

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)

# ----------------------------------------
# 2️⃣ Strings (cadenas de texto)
texto = "Python es genial"
print("\nTexto original:", texto)
print("En mayúsculas:", texto.upper())
print("En minúsculas:", texto.lower())
print("Reemplazar 'genial' por 'increíble':", texto.replace("genial", "increíble"))
print("Cantidad de caracteres:", len(texto))

# ----------------------------------------
# 3️⃣ Números: int y float
a = 10
b = 3
print("\nSuma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)     # Resultado con decimales
print("División entera:", a // b)  # Resultado sin decimales
print("Módulo (resto):", a % b)
print("Potencia:", a ** b)

# ----------------------------------------
# 4️⃣ Booleanos
tiene_permiso = True
es_mayor = edad >= 18
print("\n¿Tiene permiso?:", tiene_permiso)
print("¿Es mayor de edad?:", es_mayor)

# ----------------------------------------
# 5️⃣ Listas (mutables, ordenadas)
colores = ["rojo", "verde", "azul"]
print("\nLista de colores:", colores)
colores.append("amarillo")  # Agregar elemento
print("Lista después de agregar amarillo:", colores)
print("Primer color:", colores[0])  # Acceso por índice

# ----------------------------------------
# 6️⃣ Tuplas (inmutables, ordenadas)
coordenadas = (10, 20)
print("\nCoordenadas:", coordenadas)

# ----------------------------------------
# 7️⃣ Diccionarios (clave-valor)
persona = {"nombre": "Ana", "edad": 25}
print("\nNombre de la persona:", persona["nombre"])
persona["edad"] = 26  # Cambiar valor
print("Edad actualizada:", persona["edad"])

# ----------------------------------------
# 8️⃣ Sets (sin orden, sin duplicados)
frutas = {"manzana", "pera", "pera", "uva"}
print("\nConjunto de frutas (sin duplicados):", frutas)

# ----------------------------------------
# 9️⃣ Conversión de tipos
numero_str = "100"
numero_int = int(numero_str)
print("\nString original:", numero_str, type(numero_str))
print("Convertido a entero:", numero_int, type(numero_int))
print("Convertido a float:", float(numero_int), type(float(numero_int)))
print("Convertido a string:", str(numero_int), type(str(numero_int)))

# ----------------------------------------
# 💡 Nota: Python es de tipado dinámico
variable = 5
print("\nVariable con valor entero:", variable, type(variable))
variable = "Ahora soy un texto"
print("Variable con valor string:", variable, type(variable))
