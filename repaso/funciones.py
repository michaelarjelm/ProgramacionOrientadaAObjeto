# -----------------------------------------------------------
# FUNCIONES EN PYTHON – EJEMPLOS PRÁCTICOS
# -----------------------------------------------------------

print("\n=== 1) FUNCIÓN SIN PARÁMETROS NI RETORNO ===")
def saludar():
    """Imprime un saludo en pantalla"""
    print("Hola, mundo")

saludar()


print("\n=== 2) FUNCIÓN CON PARÁMETRO ===")
def saludar_persona(nombre):
    """Recibe un nombre y lo saluda"""
    print(f"Hola, {nombre}")

saludar_persona("Ana")
saludar_persona("Luis")


print("\n=== 3) FUNCIÓN CON RETORNO ===")
def sumar(a, b):
    """Suma dos números y devuelve el resultado"""
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)
print("La suma de 10 + 20 es:", sumar(10, 20))


print("\n=== 4) PARÁMETROS CON VALOR POR DEFECTO ===")
def saludar_con_default(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar_con_default()
saludar_con_default("Carla")


print("\n=== 5) PARÁMETROS NOMBRADOS ===")
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar("Lucía", 25)
presentar(edad=30, nombre="Pedro")  # Orden no importa si se nombran


print("\n=== 6) FUNCIÓN CON *args (argumentos variables) ===")
def sumar_todo(*numeros):
    """Recibe varios números y devuelve la suma"""
    total = 0
    for n in numeros:
        total += n
    return total

print("Suma total:", sumar_todo(1, 2, 3, 4, 5))


print("\n=== 7) FUNCIÓN CON **kwargs (argumentos con nombre) ===")
def mostrar_info(**datos):
    """Recibe pares clave-valor como diccionario"""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Madrid")


print("\n=== 8) FUNCIONES ANIDADAS ===")
def exterior():
    print("Soy la función exterior")
    def interior():
        print("Soy la función interior")
    interior()

exterior()


print("\n=== 9) FUNCIÓN LAMBDA ===")
cuadrado = lambda x: x ** 2
print("El cuadrado de 5 es:", cuadrado(5))

# Lambda con varios parámetros
sumar_lambda = lambda a, b: a + b
print("Lambda suma:", sumar_lambda(3, 7))


print("\n=== 10) FUNCIONES COMO PARÁMETROS ===")
def aplicar_funcion(funcion, valor):
    return funcion(valor)

print("Aplicar cuadrado a 6:", aplicar_funcion(cuadrado, 6))
print("Aplicar lambda anónima a 8:", aplicar_funcion(lambda n: n * 3, 8))


print("\n=== 11) MINI DESAFÍOS ===")
# A) Crear una función que reciba una lista de números y devuelva el mayor
# B) Crear una función que reciba un texto y devuelva cuántas vocales tiene
# C) Crear una función que reciba *args de strings y devuelva uno solo concatenado

print("\n--- Fin del repaso de funciones ---")
