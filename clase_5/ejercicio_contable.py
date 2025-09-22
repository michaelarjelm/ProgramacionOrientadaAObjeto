# Parte 1 – Clase base Documento
# Define una clase Documento que represente cualquier documento contable.
# Debe tener los siguientes atributos privados:
#     __id → número identificador del documento.
#     __fecha → fecha de emisión en formato texto (por ejemplo, "2025-09-07").
# Aplica encapsulamiento con @property y @setter para validar:
#     El id debe ser mayor que 0.
#     La fecha no puede estar vacía.

# --------------------------------------------------------------
# Parte 2 – Subclase Comprobante
# Crea la clase Comprobante, que herede de Documento.
# Agrega un atributo privado __monto.
# Usa @property y @setter para que el monto siempre sea mayor que 0.
# En su constructor (__init__), usa super().__init__(...) para inicializar los atributos heredados.

# --------------------------------------------------------------
# Parte 3 – Subclase Factura
# Crea la clase Factura, que herede de Comprobante.
# Agrega un atributo privado __rut_cliente.
# Define un método resumen_factura() que:
#     Use los getters heredados (id, fecha, monto).
#     Devuelva un texto con el formato: 
#     “Factura ID: 101 | Fecha: 2025-09-07 | Monto: $150000 | Cliente: 12.345.678-9"
# En su constructor (__init__), usa super().__init__(...) para inicializar lo heredado, y luego inicializa __rut_cliente.

# --------------------------------------------------------------
# Parte 4 – Demostración
# Crea una Factura válida con:
# id = 101
# fecha = "2025-09-07"
# monto = 150000
# rut_cliente = "12.345.678-9"
# Llama a resumen_factura() y muestra el resultado en pantalla.
# Intenta asignar un monto negativo y captura la excepción lanzada por el setter, 
# demostrando que el encapsulamiento está funcionando.