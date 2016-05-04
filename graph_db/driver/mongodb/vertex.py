import pqb
import uuid
from ... import types

class VertexDriver(types.BaseVertexDriver):
    def create(self, data = {}):
        vertex = {}
        uid = uuid.uuid4()
        vertex['uuid'] = vertex['_id'] =  str(uid)
        vertex['suid'] =  "%x" % (uid.fields[0])
        vertex['class'] =  data.get('class', 'V')
        vertex['type'] =  'vertex'
        vertex['data'] = data
        result = self.driver.query('vertex').insert_one(vertex)
        return vertex
    
    def update(self, criteria = {}, data = {}, **kwargs):
        mode = kwargs.get('mode', '$set')
        criteria.update({'type': 'vertex'})
        result = self.driver.query('vertex').update_many(criteria, {mode: data})
        return result

    def delete(self, criteria = {}):
        criteria.update({'type': 'vertex'})
        result = self.driver.query('vertex').delete_many(criteria)
        return result
    
    def find(self, criteria = {}):
        criteria.update({'type': 'vertex'})
        return [i for i in self.driver.query('vertex').find(criteria)]
