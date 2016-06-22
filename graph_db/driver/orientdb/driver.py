from ... import types
from . import exceptions
from . import edge
from . import vertex
import requests

class DBDriver(types.BaseDBDriver):
    def __init__(self, dbapi,settings={}):
        dbapi = dbapi(settings)
        super(DBDriver, self).__init__(dbapi)
        self.Vertex = vertex.VertexDriver(self)
        self.Edge = edge.EdgeDriver(self)

    def connect(self):
        self.dbapi.connect()
        return self

    def selectDB(self):
        self.dbapi.selectDB()
        return self

    def query(self, sql, *args, **kwargs):
        return self.dbapi.query(sql, *args, **kwargs)

    def disconnect(self):
        self.dbapi.disconnect()
        return self
