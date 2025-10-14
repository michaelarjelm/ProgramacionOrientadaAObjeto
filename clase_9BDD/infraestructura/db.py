import psycopg2
from contextlib import contextmanager
from config import DNS


def init_db():
    ddl = """
        CREATE TABLE IF NOT EXISTS cuentas  (
            id BIGSERIAL PRIMARY KEY,
            tipo VARCHAR(20) NOT NULL CHECK (tipo IN ('CUENTAAHORRO', 'CUENTACORRIENTE')),
            saldo NUMERIC(18,2) NOT NULL DEFAULT O
            );
            """
    # invocamos libreria, se conecta a la cadena de conexion (DNS)
    with psycopg2.connect(DNS) as conexion:
        with conexion.cursor() as cursor:
            # ejecuta la consulta a traves del cursor
            cursor.execute(ddl)
        # confirma los cambios
        conexion.commit()
    
@contextmanager
def get_conexion():
    conexion = psycopg2.connect(DNS)
    try:
        # 
        yield conexion
    finally:
        # cierra la conexion
        conexion.close()