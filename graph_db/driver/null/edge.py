import pqb
from ... import types
from . import exceptions
from . import utils
import uuid

class EdgeDriver(types.BaseEdgeDriver):
    def create(self, from_, to, data = {}):
        edge = {}
        uid = uuid.uuid4()
        edge['uuid'] =  str(uid)
        edge['suid'] =  "%x" % (uid.fields[0])
        edge['type'] =  'edge'
        return edge
    
    def update(self, criteria = {}, data = {}):
        return dict()

    def delete(self, eType, criteria = {}):
        return dict()

    def find(self, criteria = {}, **kwargs):
        return list()