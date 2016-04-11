from ... import types
from . import exceptions
from . import edge
from . import vertex
from pymongo import MongoClient

class DBDriver(types.BaseDBDriver):
    def __init__(self, settings={}):
        self._settings = settings
        self._settings['url'] = 'mongodb://%s:%s/%s' % (
            self._settings['host'], 
            str(self._settings['port']),
            self._settings['name']
        )
        self.Vertex = vertex.VertexDriver(self)
        self.Edge = edge.EdgeDriver(self)

    def connect(self):
        if self._connected:
            return
        self.client = MongoClient()
        self.db = self.client[self._settings['name']]
        return self

    def query(self, collection):
        if not self._connected:
            self.connect()
        return self.db[collection]

    def disconnect(self):
        if not self._connected:
            return
        self.client.close()
        return self
