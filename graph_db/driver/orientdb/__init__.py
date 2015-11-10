from . import driver
from . import vertex
from . import edge
from ...types import Map

def Factory(settings, autoConnect=False):
    DriverClass = driver.OrientDBDriver(settings=settings, autoConnect=autoConnect)
    return Map({
        'Driver': DriverClass,
        'Vertex': vertex.Vertex(DriverClass),
        'Edge': edge.Edge(DriverClass),
    })