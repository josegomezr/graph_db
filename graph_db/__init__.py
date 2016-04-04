"""
GraphDB

Almacenamiento para Grafos

Propiedades
-----------
current_connection -- Caché de la última conexión realizada
connections -- Caché de las conexiones realizadas
"""

import importlib
from . import types

current_connection = None
connections = types.Map()

def Factory(driver, settings=None, autoConnect=False):
    """
    Factory(driver_name, settings) -> DriverPackage

    Genera instancias para cada driver de GraphDB
    """
    driverModule = importlib.import_module('.driver.' + driver, __package__)
    connId = "%s-%s:%s" % (driver, settings['host'], settings['port'])

    if not connections.get(connId, False):
        if len(settings) == 0:
            raise ValueError("db: config needed")
        currentFactory = driverModule.Factory(settings, autoConnect)
        connections[connId] = current_connection = currentFactory

    return connections[connId]

__version__ = '0.0.9'
