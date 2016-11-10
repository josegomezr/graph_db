"""
GraphDB

Graph Storage and Query

@todo cache pool of connections
"""

import importlib
from . import exceptions
from . import driver

def Factory(driver, *args, **kwargs):
    """
    Factory(driver_name, settings) -> Driver

    Genera instancias para cada driver de GraphDB
    """
    driverModule = importlib.import_module('.driver.' + driver, __package__)
    return driverModule.Factory(*args, **kwargs)

__version__ = '0.0.14'
