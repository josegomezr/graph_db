
class Edge(object):
    def __init__(self, db):
        self.db = db
    
    def create(self, typeClass, From, to, data = None):
        SQL = "CREATE EDGE " + typeClass + " FROM " + From + " TO " + to
        if type(data) == dict:
            SQL = SQL + " CONTENT " + json.dumps(data)
        result = self.db.query(SQL)
        return result
    
    def update(self, typeTarget, data, criteria):
        if type(data) == dict:
            SQL = "UPDATE " + typeTarget + " CONTENT " + json.dumps(data)
        if len(criteria):
            SQL = SQL + " WHERE " + criteria
        else:
            raise Exception('ERRNODATA')
        result = self.db.query(SQL)
        return result
    
    def delete(self, typeTarget, From, to, criteria):
        SQL = "DELETE EDGE " + typeTarget + " FROM " + From + " TO " + to
        if len(criteria):
            SQL = SQL +" WHERE " + criteria
        result = self.db.query(SQL)
        return result
    
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
        result = self.driver.query(sql, depth=depth)

        return result