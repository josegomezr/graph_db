import pqb
from . import result
from ... import types

class EdgeDriver(types.BaseEdgeDriver):
    def create(self, typeClass, From, to, data = None):
        if isinstance(From, result.Result):
            From = From.get('@rid')

        if isinstance(to, result.Result):
            to = to.get('@rid')

        QB = pqb.Create('EDGE').class_(typeClass).set(data).from_(From).to(to)
        uid = uuid.uuid4()
        QB.set('uuid', str(uid))
        QB.set('suid', "%x" % (uid.fields[0]))
        QB.set('type', 'edge')
        
        SQL = QB.result()
        if self.debug:
            print SQL

        response = self.driver.query(SQL)
        res = result.Result(response[0])
        return res
    
    def update(self, typeClass, criteria, data):
        SQL = pqb.Update(typeClass).set(data).where(criteria).result()
        if self.debug:
            print SQL
        response = self.driver.query(SQL)
        return response[0]

    def search(self, typeClass, query):
        SQL = pqb.Select().from_(typeClass).where('any().toLowerCase()', '%%%s%%' % query, operator='LIKE').result()
        if self.debug:
            print SQL
        response = self.driver.query(SQL, 2)
        res = result.ResultSet(response)
        return res
    
    def delete(self, typeClass, criteria):
        SQL = pqb.Delete('EDGE').class_(typeClass).where(criteria).result()
        if self.debug:
            print SQL
        response = self.driver.query(SQL)
        return response[0]

    def find(self, typeClass, criteria = None, depth = 0):
        SQL = pqb.Select().from_(typeClass).where(criteria).result()
        if self.debug:
            print SQL
        response = self.driver.query(SQL, depth=depth)
        res = result.ResultSet(response)
        return res