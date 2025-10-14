from typing import List, Tuple
from dominio import CuentaBancaria
from infraestructura.cuentas_repositorio import CuentaRepositorio


class ServicioCuentas:
    # inyeccion de dependencias
    def __init__(self, repositorio: CuentaRepositorio):
        self._repositorio = repositorio
        
    def insertar_valores(self, cuenta: CuentaBancaria) -> int:
        return self._repositorio.insertar_valores(cuenta)
    
    def ver_tabla(self) -> List[Tuple[int, CuentaBancaria]]:
        return self._repositorio.ver_tabla()
        