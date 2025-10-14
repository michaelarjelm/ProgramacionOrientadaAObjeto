from aplicacion.servicio_cuentas import ServicioCuentas
from dominio import CuentaBancaria, CuentaCorriente
from infraestructura.cuentas_repositorio import CuentaRepositorio
from infraestructura.db import init_db


init_db()

repositorio = CuentaRepositorio()
servicio = ServicioCuentas(repositorio)

cuenta = CuentaCorriente(1000)
id_cuenta = servicio.crear(cuenta)