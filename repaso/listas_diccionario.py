# -----------------------------------------------------------
# LISTAS Y DICCIONARIOS EN PYTHON – EJEMPLOS PRÁCTICOS
# -----------------------------------------------------------

print("\n=== 1) LISTAS (list) ===")

# Crear y acceder
frutas = ["manzana", "pera", "uva"]
print("Lista inicial:", frutas)
print("Primera fruta:", frutas[0])     # manzana
print("Última fruta:", frutas[-1])     # uva

# Modificar
frutas[1] = "banana"
print("Cambio 'pera' por 'banana':", frutas)

# Agregar y quitar
frutas.append("naranja")       # agrega al final
print("append('naranja'):", frutas)

frutas.insert(1, "kiwi")       # inserta en posición 1
print("insert(1, 'kiwi'):", frutas)

frutas.remove("banana")        # elimina por valor (primera ocurrencia)
print("remove('banana'):", frutas)

eliminada = frutas.pop(0)      # elimina por índice y devuelve el valor
print("pop(0) ->", eliminada, "| lista:", frutas)

# Otras operaciones útiles
print("Largo de la lista:", len(frutas))
print("'uva' está en la lista?:", "uva" in frutas)

frutas.sort()                  # ordena (alfabético)
print("sort():", frutas)

frutas.reverse()               # invierte el orden actual
print("reverse():", frutas)

# Slicing (rebanado)
nums = [10, 20, 30, 40, 50, 60]
print("\nnums:", nums)
print("nums[1:4] ->", nums[1:4])       # 20,30,40 (fin no incluido)
print("nums[:3]  ->", nums[:3])        # 10,20,30
print("nums[::2] ->", nums[::2])       # saltos de 2

# Copia vs referencia (¡importante!)
a = [1, 2, 3]
b = a            # MISMA referencia
c = a[:]         # copia superficial
a.append(4)
print("\na:", a, "| b (misma ref):", b, "| c (copia):", c)

# Comprensión de listas (list comprehension)
cuadrados = [n*n for n in range(1, 6)]
pares = [n for n in range(10) if n % 2 == 0]
print("\nCuadrados 1..5:", cuadrados)
print("Pares < 10:", pares)

# Listas anidadas
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
print("\nMatriz:", matriz)
print("Elemento [1][2]:", matriz[1][2])  # 6

# -----------------------------------------------------------

print("\n=== 2) DICCIONARIOS (dict) ===")

# Crear y acceder
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print("Persona:", persona)
print("Nombre:", persona["nombre"])

# Agregar / modificar
persona["edad"] = 26
persona["profesion"] = "Ingeniera"
print("Actualizar edad + agregar profesión:", persona)

# Quitar
ciudad = persona.pop("ciudad")   # devuelve el valor eliminado
print("pop('ciudad') ->", ciudad, "| dict:", persona)
# del persona["edad"]  # otra forma de eliminar

# Acceso seguro
print("get('pais') ->", persona.get("pais"))                 # None si no existe
print("get('pais', 'desconocido') ->", persona.get("pais", "desconocido"))

# Recorrer claves, valores y pares
print("\nClaves:", list(persona.keys()))
print("Valores:", list(persona.values()))
print("Items:", list(persona.items()))

for clave, valor in persona.items():
    print(f"{clave} -> {valor}")

# Diccionarios anidados (JSON-like)
curso = {
    "nombre": "Python Inicial",
    "alumnos": [
        {"nombre": "Luis", "nota": 8},
        {"nombre": "Carla", "nota": 9},
    ]
}
print("\nCurso:", curso)
print("Nota de Carla:", curso["alumnos"][1]["nota"])

# Copia vs referencia en dict
original = {"a": 1, "b": [10, 20]}
copia_shallow = original.copy()          # copia superficial
original["b"].append(30)
print("\nOriginal:", original)
print("Copia superficial:", copia_shallow)  # ¡la lista interna cambió en ambos!

# Para copiar profundamente (incluye anidados):
import copy
copia_deep = copy.deepcopy(original)
original["b"].append(40)
print("Deepcopy intacta:", copia_deep)

# Comprensión de diccionarios (dict comprehension)
edades = {"Ana": 26, "Luis": 22, "Carla": 19}
mayores = {k: v for k, v in edades.items() if v >= 21}
print("\nEdades:", edades)
print("Mayores (>=21):", mayores)

# -----------------------------------------------------------

print("\n=== 3) COMBINANDO LISTAS Y DICCIONARIOS ===")

# Lista de diccionarios
productos = [
    {"id": 1, "nombre": "Mouse", "precio": 10.0},
    {"id": 2, "nombre": "Teclado", "precio": 25.0},
    {"id": 3, "nombre": "Monitor", "precio": 150.0},
]

# Filtrar productos por precio
caros = [p for p in productos if p["precio"] >= 20]
print("Productos caros (>=20):", caros)

# Índice rápido por id (de lista -> dict)
index_por_id = {p["id"]: p for p in productos}
print("Index por id:", index_por_id)
print("Producto id=2:", index_por_id[2]["nombre"])

# Actualizar un campo en todos (subir precio 10%)
for p in productos:
    p["precio"] *= 1.10
print("Precios actualizados +10%:", productos)

# -----------------------------------------------------------

print("\n=== 4) MINI DESAFÍOS (descomenta y resolvé) ===")

# A) Dada una lista de números, crear otra con solo los negativos.
# nums = [5, -2, 0, -7, 3, -1]
# negativos = ...
# print(negativos)  # [-2, -7, -1]

# B) De un dict {nombre: nota}, quedate con quienes tengan nota >= 6.
# notas = {"Ana": 9, "Luis": 5, "Carla": 7}
# aprobados = ...
# print(aprobados)  # {"Ana": 9, "Carla": 7}

# C) Convertir una lista de tuplas (clave, valor) en dict y prueba get con default.
# pares = [("a", 1), ("b", 2)]
# mi_dict = ...
# print(mi_dict.get("c", 0))  # 0

print("\n--- Fin del repaso de listas y diccionarios ---")
