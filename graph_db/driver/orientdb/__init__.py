from . import driver
from ... import exceptions
from .dbapi import OrientHTTPApi

def Factory(settings):
    """@todo docstring"""
    return driver.DBDriver(OrientHTTPApi, settings)