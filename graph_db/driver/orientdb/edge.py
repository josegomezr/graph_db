from . import result

class Edge(object):
    def __init__(self, db):
        self.db = db
    
    def create(self, typeClass, From, to, data = None):
        if isinstance(From, result.VertexResult):
            From = From.get('@rid')

        if isinstance(top, result.VertexResult):
            top = top.get('@rid')

        SQL = "CREATE EDGE " + typeClass + " FROM " + From + " TO " + to

        if type(data) == dict:
            SQL = SQL + " CONTENT " + json.dumps(data)

        response = self.db.query(SQL)
        rset = result.Result(response[0])
        return rset
    
    def update(self, typeTarget, data, criteria):
        if type(data) == dict:
            SQL = "UPDATE " + typeTarget + " CONTENT " + json.dumps(data)
        if len(criteria):
            SQL = SQL + " WHERE " + criteria
        else:
            raise Exception('ERRNODATA')
        response = self.db.query(SQL)
        return response
    
    def delete(self, typeTarget, From, to, criteria):
        SQL = "DELETE EDGE " + typeTarget + " FROM " + From + " TO " + to
        if len(criteria):
            SQL = SQL +" WHERE " + criteria
        response = self.db.query(SQL)
        return response
    
    def find(self, typeClass, criteria = None, depth = 2):
        sql = "SELECT * FROM %s" % (typeClass)
        if criteria:
            sql += " WHERE "
            n = len(criteria)
            for key, val in criteria.items():
                sql += "%s = '%s'" % (key, val)
                if n > 0:
                    n = -1
                    sql += " AND "
        response = self.driver.query(sql, depth=depth)
        rset = result.Result(response)
        return rset
