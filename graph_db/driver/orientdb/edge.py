import dquery_builder
from . import result
import uuid

class Edge(object):
    def __init__(self, driver):
        self.driver = driver

    def create(self, typeClass, From, to, data = None):
        if isinstance(From, result.Result):
            From = From.get('@rid')

        if isinstance(to, result.Result):
            to = to.get('@rid')

        SQL = dquery_builder.Create('EDGE').class_(typeClass).set(data).from_(From).to(to)
        uid = uuid.uuid4()
        SQL.set('uuid', str(uid))
        SQL.set('suid', "%x" % (uid.fields[0]))
        SQL.set('type', 'edge')
        
        response = self.driver.query(SQL.result())
        res = result.Result(response[0])
        return res
    
    def update(self, typeClass, criteria, data):
        SQL = dquery_builder.Update(typeClass).set(data).where(criteria).result()
        response = self.driver.query(SQL)
        return response[0]

    def search(self, typeClass, query):
        SQL = dquery_builder.Select().from_(typeClass).where('any().toLowerCase()', '%%%s%%' % query, operator='LIKE').result()
        response = self.driver.query(SQL, 2)
        res = result.ResultSet(response)
        return res
    
    def delete(self, typeClass, criteria):
        SQL = dquery_builder.Delete('EDGE').class_(typeClass).where(criteria).result()
        response = self.driver.query(SQL)
        return response[0]

    def find(self, typeClass, criteria = None, depth = 0):
        SQL = dquery_builder.Select().from_(typeClass).where(criteria).result()
        response = self.driver.query(SQL, depth=depth)
        res = result.ResultSet(response)
        return res