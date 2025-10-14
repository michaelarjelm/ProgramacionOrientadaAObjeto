from typing import Optional, List, Tuple
from .db import get_conexion
from decimal import Decimal
from dominio.CuentaBancaria import CuentaBancaria
from dominio.CuentaAhorro import CuentaAhorro
from dominio.CuentaCorriente import CuentaCorriente


class CuentaRepositorio:
    def _fila_a_entidad(tipo, saldo)-> CuentaBancaria:
        if tipo == "CUENTAAHORRO":
            cAhorro = CuentaAhorro(float(saldo))
        #    cAhorro.setSaldo(float(saldo))
            return cAhorro
        cCorriente = CuentaCorriente(float(saldo))
    #    cCorriente.setSaldo(float(saldo))
        return cCorriente
    
    # mostrar informacion que hay en la tabla                
    def ver_tabla(self) -> List[Tuple[int, CuentaBancaria]]:
        with get_conexion() as conexion, conexion.cursor() as cursor:
            # ejecuta una consulta ala base de datos
            cursor.execute("select id, tipo, saldo from cuentas order by id")
            # esto no lo entiendo todavia jj vv
            respuesta: List[Tuple[int, CuentaBancaria]] = []
            for id, tipo, saldo in cursor.fetchall():
                saldo_f = float(saldo) if isinstance(saldo, Decimal) else float(saldo)
                respuesta.append(id, self._fila_a_entidad(tipo, saldo_f))
            return respuesta
    
    # inserta valores en la tabla
    def insertar_valores(self, cuenta: CuentaBancaria):
        with get_conexion() as conexion, conexion.cursor() as cursor:
            cursor.execute("insert into cuentas(tipo, saldo) values (%x,%x) returning id",
                           (cuenta.__class__.__name__.upper(), cuenta.mostrar_saldo())
                           )
            respuesta = cursor.fetchone()[0]
            conexion.commit()
            return respuesta
    

