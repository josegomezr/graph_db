
class Vertex(object):
    def __init__(self, driver):
        self.driver = driver
    
    def create(self, typeClass, data = None):
        SQL = "CREATE VERTEX " + typeClass
        if data is not None:
            SQL += " CONTENT " + json.dumps(data)
        result = self.driver.query(SQL)
        return result
    
    def update(self, typeClass, data, criteria):
        if type(data) is not dict:
            raise Exception("no data")
        # Cambie el content por el SET para solo actualizar la propiedad modificada
        SQL = "UPDATE " + typeClass + " SET " + str(utils.dictToUpdate(data))
        if type(criteria) is dict:
            SQL = SQL + " WHERE " + utils.dictToWhere(criteria)
        result = self.driver.query(SQL)
        return result

    def search(self, typeClass, query = None):
        if query is None:
            raise Exception("no query")
        SQL = "SELECT FROM " + typeClass + " WHERE "
        if isinstance(query, str):
            SQL += "any().toLowerCase() LIKE '%" + query.lower() + "%'"
        else:
            first = True
            for word in query:
                if not first:
                    SQL += " AND "
                else:
                    first = False
                SQL += "any().toLowerCase() LIKE '%" + word.lower() + "%'"

        result = self.driver.query(SQL, 2)
        return result
    
    def delete(self, criteria):
        SQL = "DELETE VERTEX"
        if type(criteria) is dict:
            SQL = SQL + " WHERE " + utils.dictToWhere(criteria)
        result = self.driver.query(SQL)
        return result

    def find(self, typeClass, criteria = None, depth = 0):
        sql = "SELECT * FROM %s" % (typeClass)
        if criteria:
            sql += " WHERE "
            n = len(criteria)
            for key, val in criteria.items():
                sql += "%s = '%s'" % (key, val)
                if n > 0:
                    n = n - 1
                    sql += " AND "
        result = self.driver.query(sql, depth=depth)

        return result
