#EJERCICIO 1

# Importa las clases necesarias del archivo 'ejercicio1.py'.
from ejercicio1.libro_biblioteca import Libro, Biblioteca


    # Crea un objeto para representar nuestra biblioteca.
biblioteca_uc = Biblioteca()

    # Crea varios objetos, cada uno representando un libro.
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 5)
libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 3)

    # Invoca los métodos de la clase Biblioteca para gestionar los libros.
biblioteca_uc.agregar_libro(libro1)
biblioteca_uc.agregar_libro(libro2)
biblioteca_uc.mostrar_libros()
biblioteca_uc.prestar_libro("El Señor de los Anillos")
biblioteca_uc.devolver_libro("El Señor de los Anillos")
            

#EJERCICIO 2

# Importa las clases Alumno y Curso desde el archivo 'ejercicio2.py'.
from ejercicio2.alumno_curso import Alumno, Curso


    # Inicializa el curso que vamos a usar.
curso_poo = Curso("Programación Orientada a Objetos")

    # Crea los objetos que representan a cada alumno.
estudiante1 = Alumno("Ana García")
estudiante2 = Alumno("Luis Pérez")
estudiante3 = Alumno("Sofía Castro")

    # Llama a las funciones del curso para manejar la lista de alumnos.
curso_poo.inscribir_alumno(estudiante1)
curso_poo.inscribir_alumno(estudiante2)
curso_poo.listar_alumnos()
curso_poo.remover_alumno("Luis Pérez")
curso_poo.listar_alumnos()


#EJERCICIO 3

from ejercicio3.pedido_item import Item, Pedido


    # Crea un objeto que representa el pedido.
mi_pedido = Pedido()

    # Crea los artículos individuales del pedido.
item1 = Item("Laptop", 1200, 1)
item2 = Item("Mouse", 25, 2)
item3 = Item("Teclado", 75, 1)

    # Añade cada artículo al pedido.
mi_pedido.agregar_item(item1)
mi_pedido.agregar_item(item2)
mi_pedido.agregar_item(item3)

    # Calcula y muestra el costo total del pedido.
total_pedido = mi_pedido.calcular_total()
print(f"\nEl total del pedido es: ${total_pedido}")


#EJERCICO 4

from ejercicio4.sensor_medicion import Sensor


    # Crea una instancia para un sensor de temperatura.
sensor_temperatura = Sensor("Sensor de Temperatura")

    # Registra una serie de valores para el sensor.
sensor_temperatura.registrar_valor(25.5)
sensor_temperatura.registrar_valor(26.1)
sensor_temperatura.registrar_valor(24.8)

    # Muestra los resultados de los cálculos del sensor.
print(f"\nPromedio de temperatura: {sensor_temperatura.obtener_promedio():.2f}°C")
print(f"Temperatura máxima: {sensor_temperatura.obtener_maximo()}°C")
print(f"Temperatura mínima: {sensor_temperatura.obtener_minimo()}°C")


#EJERCICIO 5

# Trae las clases Pelicula y Catalogo para usarlas.
from ejercicio5.pelicula_catalogo import Pelicula, Catalogo


    # Crea el catálogo que contendrá las películas.
mi_catalogo = Catalogo()

    # Genera los objetos que representan las películas.
peli1 = Pelicula("Inception", "Ciencia Ficción", 2010)
peli2 = Pelicula("The Matrix", "Ciencia Ficción", 1999)
peli3 = Pelicula("Pulp Fiction", "Crimen", 1994)

    # Añade cada película a la colección.
mi_catalogo.agregar_pelicula(peli1)
mi_catalogo.agregar_pelicula(peli2)
mi_catalogo.agregar_pelicula(peli3)

    # Muestra los datos del catálogo y busca información específica.
mi_catalogo.listar_todas()
pelis_ciencia_ficcion = mi_catalogo.filtrar_por_genero("ciencia ficción")
print("\nPelículas de Ciencia Ficción:")
for p in pelis_ciencia_ficcion:
        print(f"- {p.titulo}")

peli_buscada = mi_catalogo.buscar_por_titulo("The Matrix")
if peli_buscada:
        print(f"\nEncontré: {peli_buscada.titulo}, lanzada en {peli_buscada.anio}.")


#EJERCICIO 6

# Importa las clases Usuario y Auth.
from ejercicio6.usuario_autenticacion import Usuario, Auth


    # Crea una instancia para nuestro sistema de autenticación.
sistema_auth = Auth()

    # Crea los objetos que representan a los usuarios.
usuario_nuevo = Usuario("admin", "1234")
usuario_existente = Usuario("admin", "1234")

    # Realiza las operaciones de registro y login.
sistema_auth.registrar_usuario(usuario_nuevo)
sistema_auth.registrar_usuario(usuario_existente)

print("\n--- Intento de login ---")
sistema_auth.login("admin", "1234")
sistema_auth.login("admin", "password_incorrecta")


#EJERCICIO 7

# Importa las clases Contacto y Agenda para su uso.
from ejercicio7.agenda_contacto import Contacto, Agenda


mi_agenda = Agenda()
contacto1 = Contacto("Ana", "123456789", "ana@correo.com")
contacto2 = Contacto("Luis", "987654321", "luis@correo.com")

mi_agenda.agregar_contacto(contacto1)
mi_agenda.agregar_contacto(contacto2)

mi_agenda.listar_contactos()

contacto_encontrado = mi_agenda.buscar_contacto("Ana")
if contacto_encontrado:
    print(f"\nSe encontró a Ana: {contacto_encontrado.telefono}")

mi_agenda.eliminar_contacto("Luis")
mi_agenda.listar_contactos()


#EJERCICIO 8

# Importa las clases Mesa y Restaurante.
from ejercicio8.restaurante_mesa_reserva import Mesa, Restaurante


mi_restaurante = Restaurante()
mesa1 = Mesa(1, 4)
mesa2 = Mesa(2, 6)

mi_restaurante.agregar_mesa(mesa1)
mi_restaurante.agregar_mesa(mesa2)

mi_restaurante.mostrar_estado_mesas()

mi_restaurante.reservar_mesa(1)
mi_restaurante.reservar_mesa(1)  # Vuelve a intentar reservar la misma mesa.
    
mi_restaurante.mostrar_estado_mesas()

mi_restaurante.liberar_mesa(1)
mi_restaurante.mostrar_estado_mesas()


#EJERCICIO 9

# Importa las clases Producto y Carrito.
from ejercicio9.carrito_descuento import Producto, Carrito


mi_carrito = Carrito()
prod1 = Producto("Laptop", 1200)
prod2 = Producto("Mouse", 25)

mi_carrito.agregar_producto(prod1, 1)
mi_carrito.agregar_producto(prod2, 2)
mi_carrito.agregar_producto(prod1, 1) # Agrega una unidad adicional del primer producto.

total = mi_carrito.calcular_total()
print(f"\nTotal del carrito: ${total}")

total_con_desc = mi_carrito.aplicar_descuento(10) # Calcula el total con un 10% de descuento.
print(f"Total con 10% de descuento: ${total_con_desc:.2f}")


#EJERCICIO 10

# Importa las clases Nota y Estudiante.
from ejercicio10 import Nota, Estudiante


estudiante1 = Estudiante("Carlos")
    
nota1 = Nota("Matemáticas", 8.5)
nota2 = Nota("Física", 9.0)
nota3 = Nota("Literatura", 7.5)

estudiante1.anadir_nota(nota1)
estudiante1.anadir_nota(nota2)
estudiante1.anadir_nota(nota3)

estudiante1.mostrar_calificaciones()

promedio = estudiante1.calcular_promedio()
print(f"\nEl promedio de {estudiante1.nombre} es: {promedio:.2f}")


#EJERCICIO 11

# Importa las clases Empleado y Empresa.
from ejercicio11.empleado_empresa import Empleado, Empresa


mi_empresa = Empresa()
    
empleado1 = Empleado("Pedro", 3000)
empleado2 = Empleado("María", 4500)
empleado3 = Empleado("Juan", 3200)

mi_empresa.contratar_empleado(empleado1)
mi_empresa.contratar_empleado(empleado2)
mi_empresa.contratar_empleado(empleado3)

mi_empresa.listar_empleados()

gasto_total = mi_empresa.calcular_gasto_total_sueldos()
print(f"\nGasto total de la empresa en sueldos: ${gasto_total}")


#EJERCICIO 12

# Importa las clases Cuenta y Banco.
from ejercicio12.banco_cuentas import Cuenta, Banco


mi_banco = Banco()

cuenta1 = Cuenta("Ana", 1000)
cuenta2 = Cuenta("Pedro", 500)

mi_banco.abrir_cuenta(cuenta1)
mi_banco.abrir_cuenta(cuenta2)
    
mi_banco.mostrar_estado_cuentas()

mi_banco.transferir_dinero("Ana", "Pedro", 200)
mi_banco.transferir_dinero("Pedro", "Ana", 1000) # Se espera que esta operación falle por falta de fondos.

mi_banco.mostrar_estado_cuentas()


#EJERCICIO 13

# Importa las clases Mascota y Veterinaria.
from ejercicio13.veterinaria_mascotas import Mascota, Veterinaria


mi_veterinaria = Veterinaria()
    
mascota1 = Mascota("Max", "Perro", 5)
mascota2 = Mascota("Luna", "Gato", 2)
mascota3 = Mascota("Rocky", "Perro", 8)

mi_veterinaria.registrar_mascota(mascota1)
mi_veterinaria.registrar_mascota(mascota2)
mi_veterinaria.registrar_mascota(mascota3)

mi_veterinaria.listar_todas()

edad_promedio = mi_veterinaria.calcular_edad_promedio()
print(f"\nLa edad promedio de las mascotas es: {edad_promedio:.2f} años.")


#EJERCICIO 14

# Importa las clases Pregunta y Examen.
from ejercicio14.examen_preguntas import Pregunta, Examen


mi_examen = Examen()
    
pregunta1 = Pregunta("¿Capital de Chile?", "Santiago")
pregunta2 = Pregunta("¿2 + 2 = ?", "4")
pregunta3 = Pregunta("¿Quién escribió El Quijote?", "Miguel de Cervantes")

mi_examen.anadir_pregunta(pregunta1)
mi_examen.anadir_pregunta(pregunta2)
mi_examen.anadir_pregunta(pregunta3)

mi_examen.listar_preguntas()

total_preguntas = mi_examen.contar_total_preguntas()
print(f"\nEl examen tiene un total de {total_preguntas} preguntas.")

