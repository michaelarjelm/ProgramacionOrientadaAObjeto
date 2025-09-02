# -----------------------------------------------------------
# ESTRUCTURAS DE CONTROL EN PYTHON – EJEMPLOS PRÁCTICOS
# -----------------------------------------------------------

# print("\n=== 1) CONDICIONALES (if / elif / else) ===")

# edad = 18

# if edad >= 18:
#     print("Eres mayor de edad")
# elif edad < 18:
#     print("Eres menor de edad")
# else:
#     print("Edad inválida")

# #Condicionales anidados (cuando hay más de una decisión):
# nota = 7
# if nota >= 6:
#     if nota >= 9:
#         print("Excelente")
#     else:
#         print("Aprobado")
# else:
#     print("A recuperar")

# # Operador ternario (forma corta de if/else en una línea):
# mensaje = "Par" if (nota % 2 == 0) else "Impar"
# print("La nota es:", mensaje)


#print("\n=== 2) BUCLE FOR ===")

# Recorrer una lista
frutas = ["manzana", "pera", "uva"]
# for fruta in frutas:
#     print("Me gusta la", fruta)

# Recorrer con índice usando enumerate
#for i, fruta in enumerate(frutas):
#    print(f"Índice {i} → {fruta}")

# range(inicio, fin, paso). Fin no se incluye.
#for numero in range(1, 9, 3):  # 1, 3, 5
#    print("Número impar:", numero)

# # Sumar elementos con for
# numeros = [10, 20, 30]
# suma = 0
# for n in numeros:
#     suma += n
# print("Suma =", suma)


# print("\n=== 3) BUCLE WHILE ===")

# # Repite mientras la condición sea True
# contador = 0
# while contador < 3:
#     print("Contador:", contador)
#     contador += 1  # ¡Importante! cambiar la variable, si no, bucle infinito

# # While con “bandera/sentinel”
# seguir = True
# intentos = 0
# while seguir:
#     intentos += 1
#     print("Intento", intentos)
#     if intentos == 3:
#         seguir = False
# print("Terminado con bandera.")


# print("\n=== 4) break / continue / pass ===")

# # break: corta el bucle
# for n in range(10):
#     if n == 5:
#         print("Corto en 5 con break")
#         break
#     print("n =", n)

# continue: salta a la siguiente vuelta
# for n in range(5):
#     if n == 2:
#         print("Salto el 2 con continue")
#         continue
#     print("Proceso", n)

# # pass: “no hacer nada” (sirve como placeholder)
# for n in range(3):
#     if n == 1:
#         pass  # aquí todavía no definimos qué hacer
#     else:
#         print("n distinto de 1 →", n)


# print("\n=== 5) COMBINANDO CONDICIONALES Y BUCLES ===")

# # Buscar el primer número par y cortar
# nums = [3, 7, 11, 14, 15]
# encontre_par = None
# for n in nums:
#     if n % 2 == 0:
#         encontre_par = n
#         break
# print("Primer par encontrado:", encontre_par)

# # Contar cuántas palabras tienen 4+ letras (sin detenerse)
# palabras = ["sol", "luna", "estrella", "mar"]
# conteo = 0
# for p in palabras:
#     if len(p) >= 4:
#         conteo += 1
# print("Palabras con 4+ letras:", conteo)


# print("\n=== 6) PEQUEÑAS BUENAS PRÁCTICAS ===")
# # 1) Evitar bucles infinitos: asegura que la condición cambie dentro del while.
# # 2) Prefiere for para recorrer colecciones y while para repetir hasta cierta condición.
# # 3) Usa nombres claros: 'contador', 'encontrado', 'seguir', etc.


# print("\n=== 7) MINI DESAFÍOS (para alumnos) ===")
# # Descomentar y resolver:

# # A) Dado un número n, imprime "Fizz" si es múltiplo de 3,
# #    "Buzz" si es múltiplo de 5, "FizzBuzz" si es múltiplo de 3 y 5,
# #    o el número en otro caso (usar if/elif/else).
# # n = 15
# # ...

# # B) Recorre una lista de enteros y suma solo los positivos (usar for y if).
# # numeros = [-2, 5, 0, 7, -1]
# # ...

# # C) Pide que el while se repita hasta que 'aciertos' llegue a 3 (simula aciertos sumando 1 por vuelta).
# # aciertos = 0
# # while ...:
# #     ...
# # print("¡Listo!")

# print("\n--- Fin del repaso de estructuras de control ---")
