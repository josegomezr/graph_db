import importlib

def Factory(driver, settings, autoConnect=False):
    driverModule = importlib.import_module('.driver.' + driver, __package__)
    return driverModule.Factory(settings, autoConnect)

__version__ = '0.0.1'