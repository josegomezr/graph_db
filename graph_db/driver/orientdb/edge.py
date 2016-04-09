import pqb
from ... import types
from . import exceptions
from . import utils
import uuid

class EdgeDriver(types.BaseEdgeDriver):
    def create(self, from_, to, data = {}):
        eType = data.get('class', 'E')
        
        QB = pqb.Select()
        if isinstance(from_, dict):
            from_Class, from_Value = from_.get('class', 'V'), from_.get('uuid')
        elif utils.validate_uuid4(from_):
            from_Class, from_Value = 'V', from_
        else:
            raise ValueError ('Unrecognizable Vertex Reference [%s]' % from_)

        from_ = "(%s)" % QB.from_(from_Class).where({
            'uuid': from_Value
        }).result()
       
        QB = pqb.Select()
        if isinstance(to, dict):
            toClass, toValue = to.get('class', 'V'), to.get('uuid')
        elif utils.validate_uuid4(to):
            toClass, toValue = 'V', to
        else:
            raise ValueError ('Unrecognizable Vertex Reference [%s]' % to)

        to = "(%s)" % QB.from_(toClass).where({
            'uuid': toValue
        }).result()

        QB = pqb.Create('EDGE').class_(eType).set(data).from_(from_).to(to)
        uid = uuid.uuid4()
        QB.set('uuid', str(uid))
        QB.set('suid', "%x" % (uid.fields[0]))
        QB.set('type', 'edge')
        QB.set('class', eType)
        
        SQL = QB.result()
        response = self.driver.query(SQL)
        res = response[0]
        return res
    
    def update(self, criteria = {}, data = {}):
        eType = criteria.get('class', 'E')
        SQL = pqb.Update(eType).set(data).where(criteria).result()
        response = self.driver.query(SQL)
        return response[0]

    def delete(self, eType, criteria = {}):
        eType = criteria.get('class', 'E')
        SQL = pqb.Delete('EDGE').class_(eType).where(criteria).result()
        response = self.driver.query(SQL)
        return response[0]

    def find(self, criteria = {}, **kwargs):
        depth = kwargs.get('depth', 0)
        eType = criteria.get('class', 'E')
        SQL = pqb.Select().from_(eType).where(criteria).result()
        response = self.driver.query(SQL, depth=depth)
        res = response
        return res