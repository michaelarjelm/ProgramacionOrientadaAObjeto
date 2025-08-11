# -----------------------------------------------------------
# OPERADORES BÁSICOS EN PYTHON – EJEMPLOS PRÁCTICOS
# -----------------------------------------------------------

print("\n=== 1) ARITMÉTICOS ===")
a, b = 7, 3
print("a + b =", a + b)     # 10
print("a - b =", a - b)     # 4
print("a * b =", a * b)     # 21
print("a / b =", a / b)     # 2.333... (siempre float)
print("a // b =", a // b)   # 2 (división entera, trunca)
print("a % b =", a % b)     # 1 (resto)
print("a ** b =", a ** b)   # 343 (potencia)

# Orden de operaciones (PEMDAS): ** > * / // % > + -
expr = 2 + 3 * 4 ** 2
print("2 + 3 * 4 ** 2 =", expr)  # 2 + 3 * 16 = 50
expr_parentesis = (2 + 3) * 4 ** 2
print("(2 + 3) * 4 ** 2 =", expr_parentesis)  # 5 * 16 = 80

# Cuidado con float:
x = 0.1 + 0.2
print("0.1 + 0.2 =", x, "¿Es igual a 0.3?", x == 0.3)  # Puede dar False por cómo la compu guarda los decimales


print("\n=== 2) COMPARACIÓN ===")
x, y = 5, 8
print("x == y ->", x == y)   # False
print("x != y ->", x != y)   # True
print("x > y  ->", x > y)    # False
print("x < y  ->", x < y)    # True
print("x >= 5 ->", x >= 5)   # True
print("y <= 8 ->", y <= 8)   # True

# Comparaciones encadenadas (muy Python):
n = 7
print("5 < n < 10 ->", 5 < n < 10)  # True


print("\n=== 3) LÓGICOS (and, or, not) ===")
edad = 20
tiene_dni = True
print("edad >= 18 and tiene_dni ->", edad >= 18 and tiene_dni)  # True
print("edad < 18 or tiene_dni   ->", edad < 18 or tiene_dni)    # True
print("not tiene_dni            ->", not tiene_dni)             # False

# Cortocircuito: 'and' y 'or' pueden NO evaluar la segunda parte
def caro():
    print("→ Ejecuté la función 'caro'")
    return True

print("\nCortocircuito con 'and':")
print("False and caro() ->", False and caro())  # no llama caro()

print("\nCortocircuito con 'or':")
print("True or caro()  ->", True or caro())     # no llama caro()

# 'and' y 'or' devuelven el último operando evaluado (no siempre bool):
print("\nValores devueltos por 'and'/'or':")
print("'A' and 'B' ->", "A" and "B")  # 'B'
print("'' or 'B'   ->", "" or "B")    # 'B'


print("\n=== 4) ASIGNACIÓN COMPUESTA ===")
x = 10
print("x =", x)
x += 5    # x = x + 5
x -= 3    # x = x - 3
x *= 2    # x = x * 2
x /= 4    # x = x / 4  (ojo: ahora es float)
x **= 2   # x = x ** 2
x %= 5    # x = x % 5
x //= 2   # x = x // 2 (división entera)
print("x final =", x)


print("\n=== 5) PERTENENCIA (in / not in) ===")
frutas = ["manzana", "pera", "uva"]
print("'pera' in frutas     ->", "pera" in frutas)         # True
print("'banana' not in ...  ->", "banana" not in frutas)   # True

texto = "Python es genial"
print("'genial' in texto    ->", "genial" in texto)        # True
print("'Genial' in texto    ->", "Genial" in texto)        # False (case sensitive)

# En diccionarios, 'in' busca en las CLAVES:
persona = {"nombre": "Ana", "edad": 26}
print("'nombre' in persona  ->", "nombre" in persona)      # True
print("'Ana' in persona     ->", "Ana" in persona)         # False
print("'Ana' in persona.values() ->", "Ana" in persona.values())  # True

# En sets: pertenencia es muy rápida (hash)
ids = {101, 102, 103}
print("102 in ids ->", 102 in ids)  # True


print("\n=== 6) IDENTIDAD (is / is not) ===")
a = [1, 2, 3]
b = a        # b referencia el MISMO objeto
c = [1, 2, 3]  # c es otro objeto distinto con el mismo contenido

print("a is b  ->", a is b)   # True (misma referencia)
print("a is c  ->", a is c)   # False (objetos distintos)
print("a == c  ->", a == c)   # True (contenido igual)

# Ejemplo sutil con pequeños ints/strings (interning puede hacer 'is' True):
s1 = "hola"
s2 = "hola"
print("s1 == s2 ->", s1 == s2)  # True
print("s1 is s2 ->", s1 is s2)  # A menudo True por interning, NO depender de esto


print("\n=== 7) EXTRA ÚTIL PARA CLASE ===")
# Truthiness: qué valores se consideran False al evaluar condiciones
valores = [0, 0.0, "", [], {}, set(), None, False, 1, "ok", [1], {"a":1}]
for v in valores:
    if v:
        print(repr(v), "→ se evalúa como True")
    else:
        print(repr(v), "→ se evalúa como False")

# Mini ejercicios guiados (descomentar y probar):
# 1) ¿Qué imprime y por qué?
# print( (3 > 2) and (2 > 5) or (10 // 3 == 3) )

# 2) Completa para que la condición sea True sin cambiar 'n':
# n = 12
# print( (n % 2 == 0) and (_____ in [10, 11, 12]) )

# 3) Identidad vs igualdad:
# x = [1, 2]
# y = [1, 2]
# print(x == y)   # ?
# print(x is y)   # ?

print("\n--- Fin del repaso de operadores ---")
