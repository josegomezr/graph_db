import importlib
from . import types

current_connection = None
connections = types.Map()

def Factory(driver, settings=None, autoConnect=False):
    driverModule = importlib.import_module('.driver.' + driver, __package__)

    if not connections.get(driver, False):
        if len(settings) == 0:
            raise ValueError("db: config needed")
        currentFactory = driverModule.Factory(settings, autoConnect)
        connections[driver] = current_connection = currentFactory

    return connections[driver]

__version__ = '0.0.1'