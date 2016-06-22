from . import driver
from ... import exceptions

def Factory(settings, dbapi = None):
    """@todo docstring"""
    if dbapi == None:
        import pymongo
        dbapi = pymongo

    return driver.DBDriver(dbapi, settings)