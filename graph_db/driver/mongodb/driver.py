from ... import types
from . import exceptions
from . import edge
from . import vertex

class DBDriver(types.BaseDBDriver):
    def __init__(self, settings={}):
        self.Vertex = vertex.VertexDriver(self)
        self.Edge = edge.EdgeDriver(self)
        pass

    def connect(self):
        if self._connected:
            return
        return self

    def query(self, sql, *args, **kwargs):
        if not self._connected:
            self.connect()
        return self

    def disconnect(self):
        if not self._connected:
            return
        return self
