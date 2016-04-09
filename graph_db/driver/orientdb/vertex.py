import pqb
import uuid
from ... import types

class VertexDriver(types.BaseVertexDriver):
    def create(self, data = {}):
        vType = data.get('class', 'V')
        QB = pqb.Create('VERTEX').class_(vType).set(data)
        uid = uuid.uuid4()
        QB.set('uuid', str(uid))
        QB.set('suid', "%x" % uid.fields[0])
        QB.set('type', 'vertex')
        QB.set('class', vType)
        SQL = QB.result()
        response = self.driver.query(SQL)
        res = response[0]
        return res
    
    def update(self, criteria = {}, data = {}):
        vType = criteria.get('class', 'V')
        SQL = pqb.Update(vType).set(data).where(criteria).result()
        response = self.driver.query(SQL)
        return response[0]

    def delete(self, criteria = {}):
        vType = criteria.get('class', 'V')
        SQL = pqb.Delete('VERTEX').class_(vType).where(criteria).result()
        response = self.driver.query(SQL)
        return response[0]
    
    def find(self, criteria = {}, depth = 0):
        vType = criteria.get('class', 'V')
        SQL = pqb.Select().from_(vType).where(criteria).result()
        response = self.driver.query(SQL, depth=depth)
        res = response
        return res