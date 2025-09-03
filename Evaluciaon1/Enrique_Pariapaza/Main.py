##


#EJERCICIO 7

# Importa las clases Contacto y Agenda para su uso.
from ejercicio7.agenda_contacto import Contacto, Agenda

def main_ejercicio7():
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

# Asegura que el código se ejecute solo al correr este archivo.
if __name__ == "__main__":
    main_ejercicio7()