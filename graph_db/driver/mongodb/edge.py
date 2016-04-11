from ... import types
from . import exceptions
from . import utils
import uuid
from . import vertex

class EdgeDriver(types.BaseEdgeDriver):
    def create(self, from_, to, data = {}):
        edge = {}
        uid = uuid.uuid4()
        edge['uuid'] = edge['_id'] =  str(uid)
        edge['suid'] =  "%x" % (uid.fields[0])
        
        if isinstance(from_, dict):
            from_Class, from_Value = from_.get('class', 'V'), from_.get('uuid')
        elif utils.validate_uuid4(from_):
            from_Class, from_Value = 'V', from_
        else:
            raise ValueError ('Unrecognizable Vertex Reference [%s]' % from_)

        if isinstance(to, dict):
            toClass, toValue = to.get('class', 'V'), to.get('uuid')
        elif utils.validate_uuid4(to):
            toClass, toValue = 'V', to
        else:
            raise ValueError ('Unrecognizable Vertex Reference [%s]' % to)

        edge['in'] = from_Value
        edge['out'] = toValue
        edge['type'] =  'edge'
        edge['class'] = data.get('class', 'E')


        result = self.driver.query('edge').insert_one(edge)
        
        vertex.VertexDriver(self.driver).update({'uuid': from_Value}, {'out_%s' % edge['class']: edge['uuid']}, mode='$addToSet')
        vertex.VertexDriver(self.driver).update({'uuid': toValue}, {'in_%s' % edge['class']: edge['uuid']}, mode='$addToSet')

        return edge
    
    def update(self, criteria = {}, data = {}):
        criteria.update({'type': 'edge'})
        result = self.driver.query('edge').update_many(criteria, {'$set': data})
        return result

    def delete(self, criteria = {}):
        criteria.update({'type': 'edge'})
        result = self.driver.query('edge').delete_many(criteria)
        return result
    
    def find(self, criteria = {}):
        criteria.update({'type': 'edge'})
        return [i for i in self.driver.query('edge').find(criteria)]
