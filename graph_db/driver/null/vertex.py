import pqb
import uuid
from ... import types

class VertexDriver(types.BaseVertexDriver):
    def create(self, data = {}):
        vertex = {}
        uid = uuid.uuid4()
        vertex['uuid'] =  str(uid)
        vertex['suid'] =  "%x" % (uid.fields[0])
        vertex['type'] =  'vertex'
        return vertex
    
    def update(self, criteria = {}, data = {}):
        return dict()

    def delete(self, criteria = {}):
        return dict()
    
    def find(self, criteria = {}, depth = 0):
        return list