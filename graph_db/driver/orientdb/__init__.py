from . import driver
from . import vertex
from . import edge
from ...types import Map

def Factory(settings, autoConnect=False):
    DriverInstance = driver.DBDriver(settings=settings, autoConnect=autoConnect)

    return Map({
        'DB': DriverInstance,
        'Vertex': vertex.VertexDriver(DriverInstance),
        'Edge': edge.EdgeDriver(DriverInstance),
    })