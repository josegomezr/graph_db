from . import driver
from ... import exceptions

def Factory(settings):
    """@todo docstring"""
    return driver.DBDriver(settings)