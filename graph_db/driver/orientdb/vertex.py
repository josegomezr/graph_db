import pqb
from . import result
import uuid
from ... import types

class VertexDriver(types.BaseVertexDriver):
    def create(self, typeClass, data = None):
        QB = pqb.Create('VERTEX').class_(typeClass).set(data)
        uid = uuid.uuid4()
        QB.set('uuid', str(uid))
        QB.set('suid', "%x" % uid.fields[0])
        QB.set('type', 'vertex')
        QB.set('class', typeClass)
        SQL = QB.result()

        response = self.driver.query(SQL)
        res = result.Result(response[0])
        return res
    
    def update(self, typeClass, criteria, data):
        SQL = pqb.Update(typeClass).set(data).where(criteria).result()
        response = self.driver.query(SQL)
        return result.Result(response[0])

    def search(self, typeClass, query):
        SQL = pqb.Select().from_(typeClass).where('any().toLowerCase()', '%%%s%%' % query, operator='LIKE').result()
        response = self.driver.query(SQL, 2)
        res = result.ResultSet(response)
        return res
    
    def delete(self, typeClass, criteria):
        SQL = pqb.Delete('VERTEX').class_(typeClass).where(criteria).result()
        response = self.driver.query(SQL)
        return result.Result(response[0])

    def find(self, typeClass, criteria = None, depth = 0):
        SQL = pqb.Select().from_(typeClass).where(criteria).result()
        response = self.driver.query(SQL, depth=depth)
        res = result.ResultSet(response)
        return res