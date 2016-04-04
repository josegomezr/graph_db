from . import driver
from . import vertex
from . import edge
from ...types import Map

def Factory(settings, autoConnect=False):
    DriverInstance = driver.DBDriver(settings=settings, autoConnect=autoConnect)

    Vertex = vertex.VertexDriver(DriverInstance)
    Vertex.debug = bool(settings.get('debug'))
    
    Edge = edge.EdgeDriver(DriverInstance)
    Edge.debug = bool(settings.get('debug'))

    return Map({
        'DB': DriverInstance,
        'Vertex': Vertex,
        'Edge': Edge
    })